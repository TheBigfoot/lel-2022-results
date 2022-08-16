# Rider database for London-Edinburgh-London 2022

This repository contains scripts to create a rider database for the "London-Edinburg-London 2022" cycling event.

## Prerequisites

The download script runs on bash and requires `curl` to be installed on your machine.

### Python environment

Requires `pip` and `virtualenv` (`pip` should ship with your Pytyon environment...):

```shell
$ python3 -m pip install --upgrade pip
$ python3 -m venv venv
$ . venv/bin/activate
```


## Download the driver records

In order to download the driver records from the LEL webiste, you have to login as a rider and go to the [Rider Tracking page](https://londonedinburghlondon.com/ridertracking). Now inspect the page and get yourself the cookie and the token that's used for a rider request.

Copy and paste the token into the [`get_results.sh`](./get_results.sh) script and run it in your terminal via

```shell
$ bash get_results.sh
```

This will download a bunch of HTML files into the `results` folder of this repository.

> Please note that only tracks of riders will be downloaded that registered for the race. "Did-not-starts" are not downloaded.

## Build the driver database

Run the following Python script to generate the `index.html`:

```shell
python3 lel/main.py > index.html
```

The resulting table can now be found in the [`index.html`](index.html).

## TODOs

- [x] initially sorting of table by rider ID
- [ ] allow for custom sorting
- [x] allow for searching within the table
- [ ] link to individual results
