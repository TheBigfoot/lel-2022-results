from lel.main import read_rider, read_all_riders

def test_read_user_returns_expexted_data_upon_finished_race():
    result = read_rider('testdata/finished_user.html')
    assert result.get('id') == 'AE11'
    assert result.get('name') == 'Michael Lihs'

    assert len(result.get('checkpoints')) == 21

    assert result.get('checkpoints')[0].get('time') == '12:45'
    assert result.get('checkpoints')[0].get('day') == 'Sunday'
    assert result.get('checkpoints')[0].get('name') == 'Start'

    assert result.get('checkpoints')[20].get('time') == '16:41'
    assert result.get('checkpoints')[20].get('day') == 'Friday'
    assert result.get('checkpoints')[20].get('name') == 'Debden Finish'

    assert result.get('final_checkpoint') == 'Debden Finish'
    assert result.get('end_day') == 'Friday'
    assert result.get('end_time') == '16:41'

    assert result.get('total_time') == '123:56'


def test_read_user_returns_expexted_data_for_riders_started_in_london():
    result = read_rider('testdata/finished_user_london.html')
    assert result.get('id') == 'LA1'
    assert result.get('name') == 'Sampsa Puikkonen'

    assert len(result.get('checkpoints')) == 20

    assert result.get('checkpoints')[0].get('time') == '10:10'
    assert result.get('checkpoints')[0].get('day') == 'Sunday'
    assert result.get('checkpoints')[0].get('name') == 'St Ives Northbound'

    assert result.get('checkpoints')[19].get('time') == '08:25'
    assert result.get('checkpoints')[19].get('day') == 'Friday'
    assert result.get('checkpoints')[19].get('name') == 'Debden Finish'

    assert result.get('final_checkpoint') == 'Debden Finish'
    assert result.get('end_day') == 'Friday'
    assert result.get('end_time') == '08:25'

    assert result.get('total_time') == '118:15'


def test_read_user_returns_expexted_data_upon_scratched_race():
    result = read_rider('testdata/unfinished_user.html')
    assert result.get('id') == 'AB35'
    assert result.get('name') == 'Robert Nachbaur'

    assert len(result.get('checkpoints')) == 13

    assert result.get('checkpoints')[0].get('time') == '12:00'
    assert result.get('checkpoints')[0].get('day') == 'Sunday'
    assert result.get('checkpoints')[0].get('name') == 'Start'

    assert result.get('checkpoints')[12].get('time') == '14:30'
    assert result.get('checkpoints')[12].get('day') == 'Wednesday'
    assert result.get('checkpoints')[12].get('name') == 'Brampton Southbound'

    assert result.get('final_checkpoint') == 'Brampton Southbound'
    assert result.get('end_day') == 'Wednesday'
    assert result.get('end_time') == '14:30'

    assert result.get('total_time') == '74:30'

def test_read_all_riders_returns_expected_list_of_riders():
    riders = read_all_riders('testdata')

    assert len(riders) == 2
