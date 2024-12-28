# Overview
A collection of useful applications you can self-host on your Raspberry Pi.

## Markdowner
Converts HTML to markdown.
```
/api/markdowner/scrape?url=https://example.org
```
Returns markdown in plain text.

### General

* All routes are prefixed with `/api/stats`.
* All responses will be in JSON format.
* Error messages will include a `success` flag indicating whether the request was successful or not, as well as an optional `error` message describing what went wrong.

### Endpoints

#### 1. GET /all

**Description:** Retrieves all available statistics and their values.

**Response:**

```json
{
  "success": bool,
  "data": dict
}
```

* `dict`: A dictionary containing all available statistics and their values.
* `bool`: Whether the request was successful or not (`True` for success, `False` otherwise).

#### 2. GET /get/<string:name>

**Description:** Retrieves a specific statistic by name.

**Path Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the statistic to retrieve |

**Response:**

```json
{
  "success": bool,
  "data": any
}
```

* `any`: The value of the requested statistic, or an error message if it does not exist.
* `bool`: Whether the request was successful or not (`True` for success, `False` otherwise).

#### 3. GET /history

**Description:** Retrieves a dictionary containing all available history data.

**Response:**

```json
{
  "success": bool,
  "data": dict
}
```

* `dict`: A dictionary containing all available history data.
* `bool`: Whether the request was successful or not (`True` for success, `False` otherwise).

#### 4. GET /history/<string:name>

**Description:** Retrieves a specific piece of history by name.

**Path Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `name` | string | The name of the history to retrieve |

**Response:**

```json
{
  "success": bool,
  "data": any
}
```

* `any`: The value of the requested history, or an error message if it does not exist.
* `bool`: Whether the request was successful or not (`True` for success, `False` otherwise).