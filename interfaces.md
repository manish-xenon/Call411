##API endpoints for native app

####GET /api/v1/allPhones

Returns a JSON array containing data on all phones in the database (see `getPhone` for format)

####GET /api/v1/getPhone/{model_number}  
Parameter|Value
---|---
model_number|The phone model to look up

Returns a JSON array in the following format:

Parameter|Value
---|---
model_number|The phone's model number
ram|The phone's RAM capacity (MB)
processor|The phone's CPU
manufacturer|The phone's manufacturer
system|The phone's operating system
screen_size|The phone's screen size (inches)
screen_resolution|The phone's screen resolution
battery_capacity|The phone's battery capacity (mAh)
talk_time|The phone's talk time (minutes)
camera_megapixels|The phone's camera resolution (MP)
price|The phone's price ($)
weight|The phone's weight (oz)
storage_options|The phone's storage options
dimensions|The phone's dimensions
carrier|The carriers this phone is compatible with
network_frequencies|The network frequencies this phone supports
image|URL to an image of the phone

####POST /api/v1/searchPhones  
All parameters below (sent as JSON) may either be unspecified/null or a tuple containing one or more values. If a value specifies "between these two numbers", the tuple will always have two values (if it is specified).

Parameter|Value
---|---
model_number|The phone model to look up
ram|Filter for phones with RAM between these two numbers (in MB)
processor|Filter for phones with this CPU
manufacturer|Filter for phones made by this manufacturer
system|Filter for phones with this OS
screen_size|Filter for phones with screen size between these two numbers (in inches)
screen_resolution|Filter for phones with these screen resolutions
battery_capacity|Filter for phones with battery capacity between these two numbers (in mAh)
talk_time|Filter for phones with talk time between these two numbers (in hours)
camera_megapixels|Filter for phones with camera resolution between these two numbers (in MP)
price|Filter for phones with price between these two numbers (in $)
weight|Filter for phones with weight between these two numbers (in oz)
storage_options|Filter for phones with these storage options

Returns a JSON array of search results containing data for each phone in the format specified in `getPhone`.

####GET /api/v1/similarPhones/{model_number}  
Parameter|Value
---|---
model_number|The phone model to search against

Returns a JSON array containing data for each phone similar to the phone specified using the format in `getPhone`.
