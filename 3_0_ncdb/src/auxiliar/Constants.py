##############
# Constants  #
##############

field_types=  {
                "year": {
                    "type" : "numerical",
                    "subtype" : "integer"
                    },
                "quarter":  {
                    "type": "categorical"
                    },
                "weekday": {
                    "type" : "categorical"
                        },
                "hour": {
                    "type" : "categorical"
                        },
                "vehicles_involved": {
                    "type":"numerical",
                    "subtype":"integer"
                            },
                "crash_type": {
                    "type":"categorical"
                            },
                "crash_place": {
                    "type": "categorical"
                            },
                "crash_weather": {
                    "type" : "categorical"
                            },
                "surface_state": {
                    "type": "categorical"
                            },
                "road_slope": {
                    "type": "categorical"
                            },
                "traffic_state": {
                    "type":"categorical"
                            },
                "vehicle_type": {
                    "type": "categorical"
                            },
                "vehicle_age": {
                    "type" : "numerical",
                    "subtype" : "integer"
                            },
                "passenger_sex": {
                    "type": "boolean"
                            },
                "passenger_age": {
                    "type" : "numerical",
                    "subtype" : "integer"
                            },
                "passenger_safety":{
                    "type": "categorical"
                            },
                "passenger_type": {
                    "type": "categorical"
                            },
                "fatality": {
                    "type": "boolean"
                }
}




field_transformers = {'hour': 'categorical_fuzzy',
 'crash_type': 'categorical_fuzzy',
 'crash_place': 'categorical_fuzzy',
 'crash_weather': 'categorical_fuzzy',
 'surface_state': 'categorical_fuzzy',
 'road_slope': 'categorical_fuzzy',
 'traffic_state': 'categorical_fuzzy',
 'vehicle_type': 'categorical_fuzzy',
 'passenger_sex': 'boolean',
 'passenger_safety': 'categorical_fuzzy',
 'fatality': 'boolean'}