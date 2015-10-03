API_PARAMETERS = [
    {
        "name": "year",
        "description": "Specifies the year to make calculations on. Year rates change based on federal CPI definitions. If no year is specified (i.e. <code>api?size=3</code>), it will default to the current year's requirements.",
        "required": "Not required. Default is the current year."
    },
    {
        "name": "size",
        "description": "<strong>Household size</strong> as per the <a href='#'>Healthcare.gov definition</a>.",
        "required": "Required. Must be an integer greater than 0."
    },
    {
        "name": "income",
        "description": "Integer specifying an income amount in USD.",
        "required": "Required. Must be an integer greater than 0."
    },
    {
        "name": "income_type",
        "description": "Specifies the incrementation of your income integer. monthly OR annual.",
        "required": "Not required. Defaults to 'annual'."
    }
]


 