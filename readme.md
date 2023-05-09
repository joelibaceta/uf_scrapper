# UFScrapper

UFScrapper is an API that allows you to retrieve the value of the Unidad de Fomento (UF) based on the information published on the website of the Chilean Internal Revenue Service (SII). The API is written in Flask to optimize the resources needed for its operation.

## Getting Started

In order to use UFScrapper, you will need to have Python 3 and Flask installed on your system. Once you have these dependencies installed, you can clone the repository and start using the API.

### Usage

To use the UFScrapper API, simply make a GET request to the endpoint with the date you want to retrieve the UF value, this value should be passed using query params in order to avoid date format issues. For example, to retrieve the UF value for May 8, 2021, you would make a GET request to:

```
http://127.0.0.1:5000/uf?year=2021&month=5&day=8
```

The API will return a JSON object with the UF value for the specified date. If the specified date is not available on the SII website, the API will return an error message.

```json
{
    "data": {
        "uf_value": 29525.55
    },
    "status": "success"
}
```

### Running with Docker

```
docker build -t uf_flask-app . 
```

```
docker run -it --rm -p 5000:5000 --name uf_flask-container -d uf_flask-app 
```