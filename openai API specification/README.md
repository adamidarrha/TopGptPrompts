# API Specification for OpenAI endpoints

## Overview
This document outlines the API specification for accessing the OpenAI endpoint.

## Base URL
`https://chat.openai.com`

## Endpoint: Get GPT(Gizmo) information

### URL
`/backend-api/gizmos/GPT_ID`

### Method
`GET`

### HTTP Version
`HTTP/2`

### Description
This endpoint retrieves information about the gpt, including it's openapi specification for actions, numbers of conversations the gpt had and conversation starters, files , capabilities and if it's your gpt it gives you the instructions.

### URL Parameters
- `GPT_ID`: The unique identifier for the gpt (gizmo).

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: information about the gpt.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /backend-api/gizmos/g-V2KIZSj0-ai-pdf HTTP/2
Host: chat.openai.com
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[GPT_ID](backend-api\gizmos\GPT_ID.json)

---

## Endpoint: Get GPT(Gizmo) action information

### URL
`/backend-api/gizmos/user_action_settings?gizmo_id=GPT_ID`

### Method
`GET`

### HTTP Version
`HTTP/2`

### Description
This endpoint retrieves information about the actions of the gpt and their descriptions,can tell you what actions broadly the gpt can take, all info included in the previous endpoint.

### Query Parameters
- `GPT_ID`: The unique identifier for the gpt (gizmo). example: `g-V2KIUZSj0` not the full one `g-V2KIZSj0-ai-pdf` the id without the name

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: information of the actions of the gpt.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /backend-api/gizmos/user_action_settings?gizmo_id=g-V2KIUZSj0 HTTP/2
Host: chat.openai.com
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[RESPONSE](gizmos\user_action_settings.json)

---

## Endpoint: Talk to chatgpt

### URL
`/backend-api/conversation`

### Method
`POST`

### HTTP Version
`HTTP/2`

### Description
This endpoint is the one responsible for communicating with chatgpt and retrieving response.

### Query Parameters
- `gizmo_id`: The unique identifier for the gpt (gizmo). example: `g-V2KIUZSj0` not the full one like `g-V2KIZSj0-ai-pdf` the id without the name

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: information of the actions of the gpt.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /backend-api/gizmos/user_action_settings?gizmo_id=g-V2KIUZSj0 HTTP/2
Host: chat.openai.com
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[RESPONSE](backend-api\gizmos\user_action_settings.json)

---

## Endpoint: Check if URL is safe

### URL
`/backend-api/conversation/2eaea974-969c-4d20-9fd5-73d5379f6b9b/url_safe?url=https%3A%2F%2Fmyaidrive.com%2FgGoFsP8V2dB4ArSF%2Fconstitution.pdf`

### Method
`POST`

### HTTP Version
`HTTP/2`

### Description
This endpoint is the one responsible for communicating with chatgpt and retrieving response.

### Query Parameters
- `GPT_ID`: The unique identifier for the gpt (gizmo). example: `g-V2KIUZSj0` not the full one `g-V2KIZSj0-ai-pdf` the id without the name

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: information of the actions of the gpt.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /backend-api/gizmos/user_action_settings?gizmo_id=g-V2KIUZSj0 HTTP/2
Host: chat.openai.com
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[RESPONSE](gizmos\user_action_settings.json)

---

## Endpoint: Get different prompts from openai prompt library

### URL
`/backend-api/prompt_library/`

### Method
`GET`

### HTTP Version
`HTTP/2`

### Description
This endpoint is the one responsible for giving you prompt starters , can query openai for random prompts from their prompt library up to 15 prompts.

### Query Parameters
- `limit`: the number of prompts you want to get, up to 15.
- `offset`: optional can be negative and positive don't know what's it for.

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: random prompt starters.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- **Content**: `{"detail":{"message":"Unauthorized - Access token is missing"}}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /backend-api/prompt_library/?limit=4&offset=-1 HTTP/2
Host: chat.openai.com
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[RESPONSE](backend-api\prompt_library.json)

---

/backend-api/sentinel/arkose/dx

---

## Endpoint: Get different prompts from openai prompt library

### URL
`/api/auth/session`

### Method
`GET`

### HTTP Version
`HTTP/2`

### Description
gives info about the user including the authorization token , need `__Secure-next-auth.session-token`.

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: random prompt starters.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- **Content**: `{"detail":{"message":"Unauthorized - Access token is missing"}}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /api/auth/session HTTP/2
Host: chat.openai.com
Cookie: __Secure-next-auth.session-token=<cookie>
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[RESPONSE](backend-api\prompt_library.json)

---

## Endpoint: Get different prompts from openai prompt library

### URL
`/share/{conversation_ID}`

### Method
`GET`

### HTTP Version
`HTTP/2`

### Description
gets the conversation if it's shared according to conversation id   .

### Headers
- `Authorization`: Bearer token for API access.
- `User-Agent`: Identifier for the client making the request.(NEEDED)
- `Te`: Should be set to `trailers` to indicate that the client is able to handle trailer headers in a chunked transfer encoding.(NEEDED)

### Response
#### Success Response
- **Code**: 200 OK
- **Content**: random prompt starters.

#### Error Response
- **Code**: 401 Unauthorized
- **Content**: `{"detail":"Could not parse your authentication token. Please try signing in again."}`
- **Content**: `{"detail":{"message":"Unauthorized - Access token is missing"}}`
- - **Code**: 404 Not Found
- **Content**: `{"detail":"Not found"}`

### Sample Call

GET /api/auth/session HTTP/2
Host: chat.openai.com
Cookie: __Secure-next-auth.session-token=<cookie>
User-Agent: a
Authorization: Bearer TOKEN
Te: trailers

### example response

[RESPONSE](backend-api\prompt_library.json)

---

GET /public-api/gizmos/discovery/trending?cursor=0&limit=10&locale=en
gives gizmos of trending category starting from 0 and printing 10(MAX) that are local to en , can do global or delete it.

GET /public-api/gizmos/discovery?cursor=0&limit=10&locale=global discover all gizmo of all types
/writing
/featured
/productivity
/research
/programming
/education
/lifestyles