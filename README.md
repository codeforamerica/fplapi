FPL API
=======

**Currently a proof of concept!**

The **Federal Poverty Level** is used as a base for many social services in our country. Meeting specific income levels is the first requirement to qualify for food stamps, health care, public housing subsidies, and [many other federally funded social programs](http://en.wikipedia.org/wiki/Social_programs_in_the_United_States#Types_of_social_programs).

Due to inflation and CPI, the FPL income requirements change on an annual basis, which can make relying on numbers a hassle in web applications and other software. The FPL API makes current income requirements programmatically, and reliably accessible for your applications.

## How?

*This application has not been deployed yet. A permanent URL will be accessible soon!*

**HTTP Query**
The easiest way to call the API is through a standard HTTP query with two parameters: *year* and *size*. Year is the year you wish to calculate against. If it isn't specified, the application will return the current year's income requirements. Size refers to [household size](https://www.healthcare.gov/income-and-household-information/household-size/) and is passed as an integer.

Example query:
```http
http://DOMAIN-TBD.org/api?year=2014&size=3
```

Will return a JSON response:
```javascript
{
    amount: 19790,
    amount_nice: "$19,790",
    info: {
        year_base: 11670,
        year_rate: 4060
    },
    request: {
        household_size: "3",
        year: "2014"
    }
}
```

#### *`amount`* is 100% FPL.

If no year is specified (i.e. `api?size=3`), it will default to the current year's requirements.

## API

**Use the following parameters to build a query via `/api?...`**

### `year`
Specifies the year to make calculations on. Year rates change based on federal CPI definitions.

### `size`
Household size as per the [Healthcare.gov definition](https://www.healthcare.gov/income-and-household-information/household-size/).

### `income`
Integer specifying an income amount in USD.

### `income_type`
Specifies the incrementation of your income integer. `monthly` OR `annual`. Defaults to `annual`.


## Who?

This is a side project of Team RVA, a 2015 Fellowship Team at Code for America. Inspired from a [project idea](https://github.com/codeforamerica/project-ideas/issues/70).

## Under the hood.

This is a [Flask](http://flask.pocoo.org/) application.

## Running Tests

To run tests (minimal at this point), run:

`python tests.py`

