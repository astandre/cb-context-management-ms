import unittest
from kbsbot.context_management.utils import *


class TestUtils(unittest.TestCase):

    def test_get_entities(self):
        local_interactions = [
            {
                "date": "Mon, 03 Feb 2020 14:33:41 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output":
                    {
                        "answer": {
                            "answer_type": "text",
                            "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                        },
                        "context": {
                            "entities": [
                                {
                                    "type": "http://127.0.0.1/ockb/course/ontology/Course",
                                    "value": "http://127.0.0.1/ockb/resources/EAIG5"
                                }
                            ],
                            "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                        }
                    }
                ,
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:35:47 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output":
                    {
                        "answer": {
                            "answer_type": "text",
                            "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                        },
                        "context": {
                            "entities": [
                                {
                                    "type": "http://127.0.0.1/ockb/course/ontology/Course",
                                    "value": "http://127.0.0.1/ockb/resources/EAIG5"
                                }
                            ],
                            "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                        }
                    }
                ,
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:37:44 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output": {},
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:39:16 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output": {
                    "answer": {
                        "answer_type": "text",
                        "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                    },
                    "context": {
                        "entities": [
                            {
                                "type": "http://127.0.0.1/ockb/course/ontology/Course",
                                "value": "http://127.0.0.1/ockb/resources/EAIG5"
                            }
                        ],
                        "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                    }
                },
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:40:42 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Que cursos hay"
                },
                "output": {
                    "answer": {
                        "answer_type": "text",
                        "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                    },
                    "context": {
                        "entities": [
                            {
                                "type": "http://127.0.0.1/ockb/course/ontology/Course",
                                "value": "http://127.0.0.1/ockb/resources/EAIG5"
                            }
                        ],
                        "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                    }
                },
                "social_network": 1,
                "user": 1
            }
        ]
        requires = ["http://127.0.0.1/ockb/course/ontology/Course"]
        result = get_entities(local_interactions, requires)
        self.assertTrue(len(result) > 0)
        local_interactions = [
            {
                "date": "Mon, 03 Feb 2020 14:33:41 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output":
                    {
                        "answer": {
                            "answer_type": "text",
                            "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                        },
                        "context": {
                            "entities": [

                            ],
                            "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                        }
                    }
                ,
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:35:47 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output":
                    {
                        "answer": {
                            "answer_type": "text",
                            "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                        },
                        "context": {
                            "entities": [

                            ],
                            "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                        }
                    }
                ,
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:37:44 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output": {},
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:39:16 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Cuando inicia el curso de huertos familiares"
                },
                "output": {
                    "answer": {
                        "answer_type": "text",
                        "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                    },
                    "context": {
                        "entities": [

                        ],
                        "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                    }
                },
                "social_network": 1,
                "user": 1
            },
            {
                "date": "Mon, 03 Feb 2020 14:40:42 GMT",
                "input": {
                    "context": {
                        "entities": [],
                        "intent": None
                    },
                    "user_input": "Que cursos hay"
                },
                "output": {
                    "answer": {
                        "answer_type": "text",
                        "text": " El curso denominado emprendimiento y generación de ideas se oferta con la finalidad de desarrollar conocimientos, identificar y potenciar oportunidades, para emprender e innovar en el ámbito personal, social, laboral o productivo."
                    },
                    "context": {
                        "entities": [
                        ],
                        "intent": "http://127.0.0.1/ockb/resources/ObtenerInformacion"
                    }
                },
                "social_network": 1,
                "user": 1
            }
        ]
        requires = ["http://127.0.0.1/ockb/course/ontology/Course"]
        result = get_entities(local_interactions, requires)
        self.assertTrue(len(result) == 0)
