import os.path
import re
from os import walk
import dateutil.parser
import logging
import sys

from jinja2 import Environment, FileSystemLoader

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger('LEL_LOGGER')

# <h2>Rider: AE11 Michael Lihs </h2>
id_name_pattern = re.compile(r'<h2>Rider\: (.+?) (.+?) </h2>')

# <tr> <td>Start</td> <td style="text-align: right">Sunday 12:45</td> </tr>
cp_pattern = re.compile(r'<tr> <td>(.+?)</td> <td style="text-align: right">(.+?) (\d\d:\d\d)</td> </tr>')


def output_rider_list(unsorted_riders):
    file_loader = FileSystemLoader('lel/templates')
    env = Environment(loader=file_loader)
    template = env.get_template("rider_list.html.jinja")

    unsorted_riders = read_all_riders('results/')

    sorted_riders = sorted(unsorted_riders, key=lambda d: d['sorting_id'])

    print(template.render(riders=sorted_riders))


def read_all_riders(path):
    f = []
    riders = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break

    for file in f:
        riders.append(read_rider(os.path.join(path, file)))

    return riders


def day_2_date(start_day):
    # import datetime
    # datetime.datetime.now().isoformat()
    # >>> 2020-03-20T14:28:23.382748

    if start_day == "Sunday":
        return "2022-08-07"
    elif start_day == "Monday":
        return "2022-08-08"
    elif start_day == "Tuesday":
        return "2022-08-09"
    elif start_day == "Wednesday":
        return "2022-08-10"
    elif start_day == "Thursday":
        return "2022-08-11"
    elif start_day == "Friday":
        return "2022-08-12"
    elif start_day == "Saturday":
        return "2022-08-13"
    else:
        return "not a valid finish time"


def get_total_time(checkpoints):
    if len(checkpoints) > 0:
        start_day = checkpoints[0].get('day')
        start_time = checkpoints[0].get('time')

        end_day = checkpoints[len(checkpoints) - 1].get('day')
        end_time = checkpoints[len(checkpoints) - 1].get('time')

        start_date = day_2_date(start_day)
        end_date = day_2_date(end_day)

        # import datetime
        # datetime.datetime.now().isoformat()
        # >>> 2020-03-20T14:28:23.382748

        iso_start_time_str = f"{start_date}T{start_time}:00.000000"
        iso_end_time_str = f"{end_date}T{end_time}:00.000000"

        start_datetime = dateutil.parser.isoparse(iso_start_time_str)
        end_datetime = dateutil.parser.isoparse(iso_end_time_str)

        total_time = end_datetime - start_datetime

        s = total_time.seconds + total_time.days * 24 * 3600
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02}:{:02}'.format(int(hours), int(minutes))
    else:
        return '00:00'


def get_sorting_id(id):
    letter_number_pattern = re.compile(r'([a-zA-Z]+)(\d+)')
    id_group = letter_number_pattern.search(id)
    number = id_group.group(2)
    if int(number) < 10:
        return id_group.group(1) + '0' + number
    else:
        return id


def read_rider(path):
    logger.debug(f"Reading result {path}")
    with open(path, 'r') as f:
        lines = f.read()
    id_name_group = id_name_pattern.search(lines)
    checkpoints = []
    final_checkpoint = ''
    end_day = ''
    end_time = ''
    for cp in cp_pattern.findall(lines):
        checkpoints.append({"name": cp[0], "day": cp[1], "time": cp[2]})
        final_checkpoint = cp[0]
        end_day = cp[1]
        end_time = cp[2]
    return {
        "sorting_id": get_sorting_id(id_name_group.group(1)),
        "id": id_name_group.group(1),
        "name": id_name_group.group(2),
        "checkpoints": checkpoints,
        "final_checkpoint": final_checkpoint,
        "end_day": end_day,
        "end_time": end_time,
        "total_time": get_total_time(checkpoints)
    }


def main():
    riders = read_all_riders('../results')
    output_rider_list(riders)


if __name__ == "__main__":
    main()
