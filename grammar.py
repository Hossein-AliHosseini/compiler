grammar = {
    "terminals": [
        "$",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        "/",
        ":",
        ";",
        "<",
        "=",
        "[",
        "]",
        "{",
        "}",
        "NUM",
        "ID",
        "int",
        "void",
        "break",
        "if",
        "endif",
        "else",
        "while",
        "return",
        "switch",
        "case",
        "default",
        "=="
    ],
    "non_terminals": [
        "$accept",
        "program",
        "declaration_list",
        "declaration",
        "var_declaration",
        "type_specifier",
        "fun_declaration",
        "params",
        "param_list",
        "param",
        "compound_stmt",
        "local_declarations",
        "statement_list",
        "statement",
        "expression_stmt",
        "selection_stmt",
        "iteration_stmt",
        "return_stmt",
        "switch_stmt",
        "case_stmts",
        "case_stmt",
        "default_stmt",
        "expression",
        "var",
        "simple_expression",
        "relop",
        "additive_expression",
        "addop",
        "term",
        "mulop",
        "factor",
        "call",
        "args",
        "arg_list",
        "p_operand",
        "p_num",
        "p_type",
        "p_id",
        "p_id_symbol",
        "fun_declare",
        "p_num_temp",
        "save",
        "jpf_save",
        "save_break_temp",
        "while_condition",
        "case_condition",
        "dummy_save",
        "jpf"
    ],
    "first": {
        "$accept": [
            "int",
            "void"
        ],
        "program": [
            "int",
            "void"
        ],
        "declaration_list": [
            "int",
            "void"
        ],
        "declaration": [
            "int",
            "void"
        ],
        "var_declaration": [
            "int",
            "void"
        ],
        "type_specifier": [
            "int",
            "void"
        ],
        "fun_declaration": [
            "int",
            "void"
        ],
        "params": [
            "int",
            "void"
        ],
        "param_list": [
            "int",
            "void"
        ],
        "param": [
            "int",
            "void"
        ],
        "compound_stmt": [
            "{"
        ],
        "local_declarations": [
            "int",
            "void"
        ],
        "statement_list": [
            "while",
            "switch",
            "{",
            "NUM",
            "break",
            "return",
            "if",
            "(",
            ";",
            "ID"
        ],
        "statement": [
            "while",
            "NUM",
            "break",
            "return",
            "if",
            "(",
            ";",
            "switch",
            "{",
            "ID"
        ],
        "expression_stmt": [
            "NUM",
            "break",
            "(",
            ";",
            "ID"
        ],
        "selection_stmt": [
            "if"
        ],
        "iteration_stmt": [
            "while"
        ],
        "return_stmt": [
            "return"
        ],
        "switch_stmt": [
            "switch"
        ],
        "case_stmts": [
            "case"
        ],
        "case_stmt": [
            "case"
        ],
        "default_stmt": [
            "default"
        ],
        "expression": [
            "NUM",
            "(",
            "ID"
        ],
        "var": [
            "ID"
        ],
        "simple_expression": [
            "NUM",
            "(",
            "ID"
        ],
        "relop": [
            "<",
            "=="
        ],
        "additive_expression": [
            "NUM",
            "(",
            "ID"
        ],
        "addop": [
            "-",
            "+"
        ],
        "term": [
            "NUM",
            "(",
            "ID"
        ],
        "mulop": [
            "/",
            "*"
        ],
        "factor": [
            "NUM",
            "(",
            "ID"
        ],
        "call": [
            "ID"
        ],
        "args": [
            "NUM",
            "(",
            "ID"
        ],
        "arg_list": [
            "NUM",
            "(",
            "ID"
        ],
        "p_operand": [],
        "p_num": [],
        "p_type": [],
        "p_id": [],
        "p_id_symbol": [],
        "fun_declare": [],
        "p_num_temp": [],
        "save": [],
        "jpf_save": [],
        "save_break_temp": [],
        "while_condition": [],
        "case_condition": [],
        "dummy_save": [],
        "jpf": [],
        "$": [
            "$"
        ],
        "(": [
            "("
        ],
        ")": [
            ")"
        ],
        "*": [
            "*"
        ],
        "+": [
            "+"
        ],
        ",": [
            ","
        ],
        "-": [
            "-"
        ],
        "/": [
            "/"
        ],
        ":": [
            ":"
        ],
        ";": [
            ";"
        ],
        "<": [
            "<"
        ],
        "=": [
            "="
        ],
        "[": [
            "["
        ],
        "]": [
            "]"
        ],
        "{": [
            "{"
        ],
        "}": [
            "}"
        ],
        "NUM": [
            "NUM"
        ],
        "ID": [
            "ID"
        ],
        "int": [
            "int"
        ],
        "void": [
            "void"
        ],
        "break": [
            "break"
        ],
        "if": [
            "if"
        ],
        "endif": [
            "endif"
        ],
        "else": [
            "else"
        ],
        "while": [
            "while"
        ],
        "return": [
            "return"
        ],
        "switch": [
            "switch"
        ],
        "case": [
            "case"
        ],
        "default": [
            "default"
        ],
        "==": [
            "=="
        ]
    },
    "follow": {
        "$accept": [],
        "program": [
            "$"
        ],
        "declaration_list": [
            "void",
            "int",
            "$"
        ],
        "declaration": [
            "void",
            "int",
            "$"
        ],
        "var_declaration": [
            "while",
            "void",
            "$",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "int",
            "return",
            "if",
            "(",
            ";",
            "ID"
        ],
        "type_specifier": [
            "ID"
        ],
        "fun_declaration": [
            "void",
            "int",
            "$"
        ],
        "params": [
            ")"
        ],
        "param_list": [
            ")",
            ","
        ],
        "param": [
            ")",
            ","
        ],
        "compound_stmt": [
            "while",
            "endif",
            "void",
            "else",
            "$",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "int",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "local_declarations": [
            "while",
            "void",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "int",
            "return",
            "if",
            "(",
            ";",
            "ID"
        ],
        "statement_list": [
            "while",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "statement": [
            "while",
            "endif",
            "else",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "expression_stmt": [
            "while",
            "endif",
            "else",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "selection_stmt": [
            "while",
            "endif",
            "else",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "iteration_stmt": [
            "while",
            "endif",
            "else",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "return_stmt": [
            "while",
            "endif",
            "else",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "switch_stmt": [
            "while",
            "endif",
            "else",
            "switch",
            "{",
            "NUM",
            "}",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "case_stmts": [
            "case",
            "default"
        ],
        "case_stmt": [
            "case",
            "default"
        ],
        "default_stmt": [
            "}"
        ],
        "expression": [
            ",",
            "]",
            ")",
            ";"
        ],
        "var": [
            ")",
            "*",
            "-",
            ",",
            "+",
            "==",
            "/",
            "]",
            ";",
            "<",
            "="
        ],
        "simple_expression": [
            ",",
            "]",
            ")",
            ";"
        ],
        "relop": [
            "NUM",
            "(",
            "ID"
        ],
        "additive_expression": [
            "+",
            ")",
            "-",
            "==",
            "]",
            ",",
            ";",
            "<"
        ],
        "addop": [
            "NUM",
            "(",
            "ID"
        ],
        "term": [
            "+",
            ")",
            "*",
            "-",
            "==",
            "/",
            "]",
            ",",
            ";",
            "<"
        ],
        "mulop": [
            "NUM",
            "(",
            "ID"
        ],
        "factor": [
            ")",
            "*",
            "-",
            ",",
            "+",
            "==",
            "/",
            "]",
            ";",
            "<"
        ],
        "call": [
            ")",
            "*",
            "-",
            ",",
            "+",
            "==",
            "/",
            "]",
            ";",
            "<"
        ],
        "args": [
            ")"
        ],
        "arg_list": [
            ")",
            ","
        ],
        "p_operand": [
            "+",
            "/",
            "*",
            "-",
            "<",
            "=="
        ],
        "p_num": [
            "NUM"
        ],
        "p_type": [
            "int",
            "void"
        ],
        "p_id": [
            "ID"
        ],
        "p_id_symbol": [
            "ID"
        ],
        "fun_declare": [
            "{"
        ],
        "p_num_temp": [
            "NUM"
        ],
        "save": [
            "while",
            "switch",
            "{",
            "NUM",
            "break",
            "default",
            "return",
            "case",
            "if",
            "(",
            ";",
            "ID"
        ],
        "jpf_save": [
            "while",
            "switch",
            "{",
            "NUM",
            "break",
            "return",
            "if",
            "(",
            ";",
            "ID"
        ],
        "save_break_temp": [
            "("
        ],
        "while_condition": [
            "while",
            "switch",
            "{",
            "NUM",
            "break",
            "return",
            "if",
            "(",
            ";",
            "ID"
        ],
        "case_condition": [
            "NUM"
        ],
        "dummy_save": [
            "{"
        ],
        "jpf": [
            "}",
            "case",
            "default"
        ]
    },
    "grammar": {
        "0": [
            "$accept",
            "->",
            "program",
            "$"
        ],
        "1": [
            "program",
            "->",
            "declaration_list"
        ],
        "2": [
            "declaration_list",
            "->",
            "declaration_list",
            "declaration"
        ],
        "3": [
            "declaration_list",
            "->",
            "declaration"
        ],
        "4": [
            "declaration",
            "->",
            "var_declaration"
        ],
        "5": [
            "declaration",
            "->",
            "fun_declaration"
        ],
        "6": [
            "var_declaration",
            "->",
            "type_specifier",
            "p_id_symbol",
            "ID",
            ";"
        ],
        "7": [
            "var_declaration",
            "->",
            "type_specifier",
            "p_id_symbol",
            "ID",
            "[",
            "p_num",
            "NUM",
            "]",
            ";"
        ],
        "8": [
            "type_specifier",
            "->",
            "p_type",
            "int"
        ],
        "9": [
            "type_specifier",
            "->",
            "p_type",
            "void"
        ],
        "10": [
            "fun_declaration",
            "->",
            "type_specifier",
            "p_id_symbol",
            "ID",
            "(",
            "params",
            ")",
            "fun_declare",
            "compound_stmt"
        ],
        "11": [
            "params",
            "->",
            "param_list"
        ],
        "12": [
            "params",
            "->",
            "p_type",
            "void"
        ],
        "13": [
            "param_list",
            "->",
            "param_list",
            ",",
            "param"
        ],
        "14": [
            "param_list",
            "->",
            "param"
        ],
        "15": [
            "param",
            "->",
            "type_specifier",
            "ID"
        ],
        "16": [
            "param",
            "->",
            "type_specifier",
            "ID",
            "[",
            "]"
        ],
        "17": [
            "compound_stmt",
            "->",
            "{",
            "local_declarations",
            "statement_list",
            "}"
        ],
        "18": [
            "local_declarations",
            "->",
            "local_declarations",
            "var_declaration"
        ],
        "19": [
            "local_declarations",
            "->",
            "epsilon"
        ],
        "20": [
            "statement_list",
            "->",
            "statement_list",
            "statement"
        ],
        "21": [
            "statement_list",
            "->",
            "epsilon"
        ],
        "22": [
            "statement",
            "->",
            "expression_stmt"
        ],
        "23": [
            "statement",
            "->",
            "compound_stmt"
        ],
        "24": [
            "statement",
            "->",
            "selection_stmt"
        ],
        "25": [
            "statement",
            "->",
            "iteration_stmt"
        ],
        "26": [
            "statement",
            "->",
            "return_stmt"
        ],
        "27": [
            "statement",
            "->",
            "switch_stmt"
        ],
        "28": [
            "expression_stmt",
            "->",
            "expression",
            ";"
        ],
        "29": [
            "expression_stmt",
            "->",
            "break",
            ";"
        ],
        "30": [
            "expression_stmt",
            "->",
            ";"
        ],
        "31": [
            "selection_stmt",
            "->",
            "if",
            "(",
            "expression",
            ")",
            "save",
            "statement",
            "endif"
        ],
        "32": [
            "selection_stmt",
            "->",
            "if",
            "(",
            "expression",
            ")",
            "save",
            "statement",
            "else",
            "jpf_save",
            "statement",
            "endif"
        ],
        "33": [
            "iteration_stmt",
            "->",
            "while",
            "save",
            "save_break_temp",
            "(",
            "expression",
            ")",
            "while_condition",
            "statement"
        ],
        "34": [
            "return_stmt",
            "->",
            "return",
            ";"
        ],
        "35": [
            "return_stmt",
            "->",
            "return",
            "expression",
            ";"
        ],
        "36": [
            "switch_stmt",
            "->",
            "switch",
            "save",
            "save_break_temp",
            "(",
            "expression",
            ")",
            "dummy_save",
            "{",
            "case_stmts",
            "default_stmt",
            "}"
        ],
        "37": [
            "case_stmts",
            "->",
            "case_stmts",
            "case_stmt"
        ],
        "38": [
            "case_stmts",
            "->",
            "epsilon"
        ],
        "39": [
            "case_stmt",
            "->",
            "jpf",
            "case",
            "case_condition",
            "NUM",
            ":",
            "save",
            "statement_list"
        ],
        "40": [
            "default_stmt",
            "->",
            "jpf",
            "default",
            ":",
            "statement_list"
        ],
        "41": [
            "default_stmt",
            "->",
            "jpf"
        ],
        "42": [
            "expression",
            "->",
            "var",
            "=",
            "expression"
        ],
        "43": [
            "expression",
            "->",
            "simple_expression"
        ],
        "44": [
            "var",
            "->",
            "p_id",
            "ID"
        ],
        "45": [
            "var",
            "->",
            "p_id",
            "ID",
            "[",
            "expression",
            "]"
        ],
        "46": [
            "simple_expression",
            "->",
            "additive_expression",
            "relop",
            "additive_expression"
        ],
        "47": [
            "simple_expression",
            "->",
            "additive_expression"
        ],
        "48": [
            "relop",
            "->",
            "p_operand",
            "<"
        ],
        "49": [
            "relop",
            "->",
            "p_operand",
            "=="
        ],
        "50": [
            "additive_expression",
            "->",
            "additive_expression",
            "addop",
            "term"
        ],
        "51": [
            "additive_expression",
            "->",
            "term"
        ],
        "52": [
            "addop",
            "->",
            "p_operand",
            "+"
        ],
        "53": [
            "addop",
            "->",
            "p_operand",
            "-"
        ],
        "54": [
            "term",
            "->",
            "term",
            "mulop",
            "factor"
        ],
        "55": [
            "term",
            "->",
            "factor"
        ],
        "56": [
            "mulop",
            "->",
            "p_operand",
            "*"
        ],
        "57": [
            "mulop",
            "->",
            "p_operand",
            "/"
        ],
        "58": [
            "factor",
            "->",
            "(",
            "expression",
            ")"
        ],
        "59": [
            "factor",
            "->",
            "var"
        ],
        "60": [
            "factor",
            "->",
            "call"
        ],
        "61": [
            "factor",
            "->",
            "p_num_temp",
            "NUM"
        ],
        "62": [
            "call",
            "->",
            "p_id",
            "ID",
            "(",
            "args",
            ")"
        ],
        "63": [
            "args",
            "->",
            "arg_list"
        ],
        "64": [
            "args",
            "->",
            "epsilon"
        ],
        "65": [
            "arg_list",
            "->",
            "arg_list",
            ",",
            "expression"
        ],
        "66": [
            "arg_list",
            "->",
            "expression"
        ],
        "67": [
            "p_operand",
            "->",
            "epsilon"
        ],
        "68": [
            "p_num",
            "->",
            "epsilon"
        ],
        "69": [
            "p_type",
            "->",
            "epsilon"
        ],
        "70": [
            "p_id",
            "->",
            "epsilon"
        ],
        "71": [
            "p_id_symbol",
            "->",
            "epsilon"
        ],
        "72": [
            "fun_declare",
            "->",
            "epsilon"
        ],
        "73": [
            "p_num_temp",
            "->",
            "epsilon"
        ],
        "74": [
            "save",
            "->",
            "epsilon"
        ],
        "75": [
            "jpf_save",
            "->",
            "epsilon"
        ],
        "76": [
            "save_break_temp",
            "->",
            "epsilon"
        ],
        "77": [
            "while_condition",
            "->",
            "epsilon"
        ],
        "78": [
            "case_condition",
            "->",
            "epsilon"
        ],
        "79": [
            "dummy_save",
            "->",
            "epsilon"
        ],
        "80": [
            "jpf",
            "->",
            "epsilon"
        ]
    },
    "parse_table": {
        "0": {
            "program": "goto_1",
            "declaration_list": "goto_2",
            "declaration": "goto_3",
            "var_declaration": "goto_4",
            "type_specifier": "goto_5",
            "fun_declaration": "goto_6",
            "p_type": "goto_7",
            "int": "reduce_69",
            "void": "reduce_69"
        },
        "1": {
            "$": "shift_8"
        },
        "2": {
            "declaration": "goto_9",
            "var_declaration": "goto_4",
            "type_specifier": "goto_5",
            "fun_declaration": "goto_6",
            "p_type": "goto_7",
            "$": "reduce_1",
            "int": "reduce_69",
            "void": "reduce_69"
        },
        "3": {
            "void": "reduce_3",
            "int": "reduce_3",
            "$": "reduce_3"
        },
        "4": {
            "void": "reduce_4",
            "int": "reduce_4",
            "$": "reduce_4"
        },
        "5": {
            "p_id_symbol": "goto_10",
            "ID": "reduce_71"
        },
        "6": {
            "void": "reduce_5",
            "int": "reduce_5",
            "$": "reduce_5"
        },
        "7": {
            "int": "shift_11",
            "void": "shift_12"
        },
        "8": {
            "$": "accept"
        },
        "9": {
            "void": "reduce_2",
            "int": "reduce_2",
            "$": "reduce_2"
        },
        "10": {
            "ID": "shift_13"
        },
        "11": {
            "ID": "reduce_8"
        },
        "12": {
            "ID": "reduce_9"
        },
        "13": {
            ";": "shift_14",
            "[": "shift_15",
            "(": "shift_16"
        },
        "14": {
            "while": "reduce_6",
            "void": "reduce_6",
            "$": "reduce_6",
            "switch": "reduce_6",
            "{": "reduce_6",
            "NUM": "reduce_6",
            "}": "reduce_6",
            "break": "reduce_6",
            "int": "reduce_6",
            "return": "reduce_6",
            "if": "reduce_6",
            "(": "reduce_6",
            ";": "reduce_6",
            "ID": "reduce_6"
        },
        "15": {
            "p_num": "goto_17",
            "NUM": "reduce_68"
        },
        "16": {
            "type_specifier": "goto_18",
            "params": "goto_19",
            "param_list": "goto_20",
            "param": "goto_21",
            "p_type": "goto_22",
            "int": "reduce_69",
            "void": "reduce_69"
        },
        "17": {
            "NUM": "shift_23"
        },
        "18": {
            "ID": "shift_24"
        },
        "19": {
            ")": "shift_25"
        },
        "20": {
            ",": "shift_26",
            ")": "reduce_11"
        },
        "21": {
            ")": "reduce_14",
            ",": "reduce_14"
        },
        "22": {
            "int": "shift_11",
            "void": "shift_27"
        },
        "23": {
            "]": "shift_28"
        },
        "24": {
            "[": "shift_29",
            ")": "reduce_15",
            ",": "reduce_15"
        },
        "25": {
            "fun_declare": "goto_30",
            "{": "reduce_72"
        },
        "26": {
            "type_specifier": "goto_18",
            "param": "goto_31",
            "p_type": "goto_7",
            "int": "reduce_69",
            "void": "reduce_69"
        },
        "27": {
            ")": "reduce_12",
            "ID": "reduce_9"
        },
        "28": {
            ";": "shift_32"
        },
        "29": {
            "]": "shift_33"
        },
        "30": {
            "{": "shift_34",
            "compound_stmt": "goto_35"
        },
        "31": {
            ")": "reduce_13",
            ",": "reduce_13"
        },
        "32": {
            "while": "reduce_7",
            "void": "reduce_7",
            "$": "reduce_7",
            "switch": "reduce_7",
            "{": "reduce_7",
            "NUM": "reduce_7",
            "}": "reduce_7",
            "break": "reduce_7",
            "int": "reduce_7",
            "return": "reduce_7",
            "if": "reduce_7",
            "(": "reduce_7",
            ";": "reduce_7",
            "ID": "reduce_7"
        },
        "33": {
            ")": "reduce_16",
            ",": "reduce_16"
        },
        "34": {
            "local_declarations": "goto_36",
            "while": "reduce_19",
            "void": "reduce_19",
            "switch": "reduce_19",
            "{": "reduce_19",
            "NUM": "reduce_19",
            "}": "reduce_19",
            "break": "reduce_19",
            "int": "reduce_19",
            "return": "reduce_19",
            "if": "reduce_19",
            "(": "reduce_19",
            ";": "reduce_19",
            "ID": "reduce_19"
        },
        "35": {
            "void": "reduce_10",
            "int": "reduce_10",
            "$": "reduce_10"
        },
        "36": {
            "var_declaration": "goto_37",
            "type_specifier": "goto_38",
            "statement_list": "goto_39",
            "p_type": "goto_7",
            "int": "reduce_69",
            "void": "reduce_69",
            "while": "reduce_21",
            "switch": "reduce_21",
            "{": "reduce_21",
            "NUM": "reduce_21",
            "}": "reduce_21",
            "break": "reduce_21",
            "default": "reduce_21",
            "return": "reduce_21",
            "case": "reduce_21",
            "if": "reduce_21",
            "(": "reduce_21",
            ";": "reduce_21",
            "ID": "reduce_21"
        },
        "37": {
            "while": "reduce_18",
            "void": "reduce_18",
            "switch": "reduce_18",
            "{": "reduce_18",
            "NUM": "reduce_18",
            "}": "reduce_18",
            "break": "reduce_18",
            "int": "reduce_18",
            "return": "reduce_18",
            "if": "reduce_18",
            "(": "reduce_18",
            ";": "reduce_18",
            "ID": "reduce_18"
        },
        "38": {
            "p_id_symbol": "goto_40",
            "ID": "reduce_71"
        },
        "39": {
            ";": "shift_41",
            "(": "shift_42",
            "{": "shift_34",
            "}": "shift_43",
            "break": "shift_44",
            "if": "shift_45",
            "while": "shift_46",
            "return": "shift_47",
            "switch": "shift_48",
            "compound_stmt": "goto_49",
            "statement": "goto_50",
            "expression_stmt": "goto_51",
            "selection_stmt": "goto_52",
            "iteration_stmt": "goto_53",
            "return_stmt": "goto_54",
            "switch_stmt": "goto_55",
            "expression": "goto_56",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "40": {
            "ID": "shift_65"
        },
        "41": {
            "while": "reduce_30",
            "endif": "reduce_30",
            "else": "reduce_30",
            "switch": "reduce_30",
            "{": "reduce_30",
            "NUM": "reduce_30",
            "}": "reduce_30",
            "break": "reduce_30",
            "default": "reduce_30",
            "return": "reduce_30",
            "case": "reduce_30",
            "if": "reduce_30",
            "(": "reduce_30",
            ";": "reduce_30",
            "ID": "reduce_30"
        },
        "42": {
            "(": "shift_42",
            "expression": "goto_66",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "43": {
            "while": "reduce_17",
            "endif": "reduce_17",
            "void": "reduce_17",
            "else": "reduce_17",
            "$": "reduce_17",
            "switch": "reduce_17",
            "{": "reduce_17",
            "NUM": "reduce_17",
            "}": "reduce_17",
            "break": "reduce_17",
            "default": "reduce_17",
            "int": "reduce_17",
            "return": "reduce_17",
            "case": "reduce_17",
            "if": "reduce_17",
            "(": "reduce_17",
            ";": "reduce_17",
            "ID": "reduce_17"
        },
        "44": {
            ";": "shift_67"
        },
        "45": {
            "(": "shift_68"
        },
        "46": {
            "save": "goto_69",
            "while": "reduce_74",
            "switch": "reduce_74",
            "{": "reduce_74",
            "NUM": "reduce_74",
            "break": "reduce_74",
            "default": "reduce_74",
            "return": "reduce_74",
            "case": "reduce_74",
            "if": "reduce_74",
            "(": "reduce_74",
            ";": "reduce_74",
            "ID": "reduce_74"
        },
        "47": {
            ";": "shift_70",
            "(": "shift_42",
            "expression": "goto_71",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "48": {
            "save": "goto_72",
            "while": "reduce_74",
            "switch": "reduce_74",
            "{": "reduce_74",
            "NUM": "reduce_74",
            "break": "reduce_74",
            "default": "reduce_74",
            "return": "reduce_74",
            "case": "reduce_74",
            "if": "reduce_74",
            "(": "reduce_74",
            ";": "reduce_74",
            "ID": "reduce_74"
        },
        "49": {
            "while": "reduce_23",
            "endif": "reduce_23",
            "else": "reduce_23",
            "switch": "reduce_23",
            "{": "reduce_23",
            "NUM": "reduce_23",
            "}": "reduce_23",
            "break": "reduce_23",
            "default": "reduce_23",
            "return": "reduce_23",
            "case": "reduce_23",
            "if": "reduce_23",
            "(": "reduce_23",
            ";": "reduce_23",
            "ID": "reduce_23"
        },
        "50": {
            "while": "reduce_20",
            "switch": "reduce_20",
            "{": "reduce_20",
            "NUM": "reduce_20",
            "}": "reduce_20",
            "break": "reduce_20",
            "default": "reduce_20",
            "return": "reduce_20",
            "case": "reduce_20",
            "if": "reduce_20",
            "(": "reduce_20",
            ";": "reduce_20",
            "ID": "reduce_20"
        },
        "51": {
            "while": "reduce_22",
            "endif": "reduce_22",
            "else": "reduce_22",
            "switch": "reduce_22",
            "{": "reduce_22",
            "NUM": "reduce_22",
            "}": "reduce_22",
            "break": "reduce_22",
            "default": "reduce_22",
            "return": "reduce_22",
            "case": "reduce_22",
            "if": "reduce_22",
            "(": "reduce_22",
            ";": "reduce_22",
            "ID": "reduce_22"
        },
        "52": {
            "while": "reduce_24",
            "endif": "reduce_24",
            "else": "reduce_24",
            "switch": "reduce_24",
            "{": "reduce_24",
            "NUM": "reduce_24",
            "}": "reduce_24",
            "break": "reduce_24",
            "default": "reduce_24",
            "return": "reduce_24",
            "case": "reduce_24",
            "if": "reduce_24",
            "(": "reduce_24",
            ";": "reduce_24",
            "ID": "reduce_24"
        },
        "53": {
            "while": "reduce_25",
            "endif": "reduce_25",
            "else": "reduce_25",
            "switch": "reduce_25",
            "{": "reduce_25",
            "NUM": "reduce_25",
            "}": "reduce_25",
            "break": "reduce_25",
            "default": "reduce_25",
            "return": "reduce_25",
            "case": "reduce_25",
            "if": "reduce_25",
            "(": "reduce_25",
            ";": "reduce_25",
            "ID": "reduce_25"
        },
        "54": {
            "while": "reduce_26",
            "endif": "reduce_26",
            "else": "reduce_26",
            "switch": "reduce_26",
            "{": "reduce_26",
            "NUM": "reduce_26",
            "}": "reduce_26",
            "break": "reduce_26",
            "default": "reduce_26",
            "return": "reduce_26",
            "case": "reduce_26",
            "if": "reduce_26",
            "(": "reduce_26",
            ";": "reduce_26",
            "ID": "reduce_26"
        },
        "55": {
            "while": "reduce_27",
            "endif": "reduce_27",
            "else": "reduce_27",
            "switch": "reduce_27",
            "{": "reduce_27",
            "NUM": "reduce_27",
            "}": "reduce_27",
            "break": "reduce_27",
            "default": "reduce_27",
            "return": "reduce_27",
            "case": "reduce_27",
            "if": "reduce_27",
            "(": "reduce_27",
            ";": "reduce_27",
            "ID": "reduce_27"
        },
        "56": {
            ";": "shift_73"
        },
        "57": {
            "=": "shift_74",
            ")": "reduce_59",
            "*": "reduce_59",
            "-": "reduce_59",
            ",": "reduce_59",
            "+": "reduce_59",
            "==": "reduce_59",
            "/": "reduce_59",
            "]": "reduce_59",
            ";": "reduce_59",
            "<": "reduce_59"
        },
        "58": {
            ",": "reduce_43",
            "]": "reduce_43",
            ")": "reduce_43",
            ";": "reduce_43"
        },
        "59": {
            "relop": "goto_75",
            "addop": "goto_76",
            "p_operand": "goto_77",
            "+": "reduce_67",
            "/": "reduce_67",
            "*": "reduce_67",
            "-": "reduce_67",
            "<": "reduce_67",
            "==": "reduce_67",
            ",": "reduce_47",
            "]": "reduce_47",
            ")": "reduce_47",
            ";": "reduce_47"
        },
        "60": {
            "mulop": "goto_78",
            "p_operand": "goto_79",
            "+": "reduce_51",
            "/": "reduce_67",
            "*": "reduce_67",
            "-": "reduce_51",
            "<": "reduce_51",
            "==": "reduce_51",
            ")": "reduce_51",
            "]": "reduce_51",
            ",": "reduce_51",
            ";": "reduce_51"
        },
        "61": {
            "+": "reduce_55",
            ")": "reduce_55",
            "*": "reduce_55",
            "-": "reduce_55",
            "==": "reduce_55",
            "/": "reduce_55",
            "]": "reduce_55",
            ",": "reduce_55",
            ";": "reduce_55",
            "<": "reduce_55"
        },
        "62": {
            ")": "reduce_60",
            "*": "reduce_60",
            "-": "reduce_60",
            ",": "reduce_60",
            "+": "reduce_60",
            "==": "reduce_60",
            "/": "reduce_60",
            "]": "reduce_60",
            ";": "reduce_60",
            "<": "reduce_60"
        },
        "63": {
            "ID": "shift_80"
        },
        "64": {
            "NUM": "shift_81"
        },
        "65": {
            ";": "shift_14",
            "[": "shift_15"
        },
        "66": {
            ")": "shift_82"
        },
        "67": {
            "while": "reduce_29",
            "endif": "reduce_29",
            "else": "reduce_29",
            "switch": "reduce_29",
            "{": "reduce_29",
            "NUM": "reduce_29",
            "}": "reduce_29",
            "break": "reduce_29",
            "default": "reduce_29",
            "return": "reduce_29",
            "case": "reduce_29",
            "if": "reduce_29",
            "(": "reduce_29",
            ";": "reduce_29",
            "ID": "reduce_29"
        },
        "68": {
            "(": "shift_42",
            "expression": "goto_83",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "69": {
            "save_break_temp": "goto_84",
            "(": "reduce_76"
        },
        "70": {
            "while": "reduce_34",
            "endif": "reduce_34",
            "else": "reduce_34",
            "switch": "reduce_34",
            "{": "reduce_34",
            "NUM": "reduce_34",
            "}": "reduce_34",
            "break": "reduce_34",
            "default": "reduce_34",
            "return": "reduce_34",
            "case": "reduce_34",
            "if": "reduce_34",
            "(": "reduce_34",
            ";": "reduce_34",
            "ID": "reduce_34"
        },
        "71": {
            ";": "shift_85"
        },
        "72": {
            "save_break_temp": "goto_86",
            "(": "reduce_76"
        },
        "73": {
            "while": "reduce_28",
            "endif": "reduce_28",
            "else": "reduce_28",
            "switch": "reduce_28",
            "{": "reduce_28",
            "NUM": "reduce_28",
            "}": "reduce_28",
            "break": "reduce_28",
            "default": "reduce_28",
            "return": "reduce_28",
            "case": "reduce_28",
            "if": "reduce_28",
            "(": "reduce_28",
            ";": "reduce_28",
            "ID": "reduce_28"
        },
        "74": {
            "(": "shift_42",
            "expression": "goto_87",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "75": {
            "(": "shift_42",
            "var": "goto_88",
            "additive_expression": "goto_89",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "76": {
            "(": "shift_42",
            "var": "goto_88",
            "term": "goto_90",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "77": {
            "<": "shift_91",
            "==": "shift_92",
            "+": "shift_93",
            "-": "shift_94"
        },
        "78": {
            "(": "shift_42",
            "var": "goto_88",
            "factor": "goto_95",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "79": {
            "*": "shift_96",
            "/": "shift_97"
        },
        "80": {
            "[": "shift_98",
            "(": "shift_99",
            ")": "reduce_44",
            "*": "reduce_44",
            "-": "reduce_44",
            ",": "reduce_44",
            "+": "reduce_44",
            "==": "reduce_44",
            "/": "reduce_44",
            "]": "reduce_44",
            ";": "reduce_44",
            "<": "reduce_44",
            "=": "reduce_44"
        },
        "81": {
            ")": "reduce_61",
            "*": "reduce_61",
            "-": "reduce_61",
            ",": "reduce_61",
            "+": "reduce_61",
            "==": "reduce_61",
            "/": "reduce_61",
            "]": "reduce_61",
            ";": "reduce_61",
            "<": "reduce_61"
        },
        "82": {
            ")": "reduce_58",
            "*": "reduce_58",
            "-": "reduce_58",
            ",": "reduce_58",
            "+": "reduce_58",
            "==": "reduce_58",
            "/": "reduce_58",
            "]": "reduce_58",
            ";": "reduce_58",
            "<": "reduce_58"
        },
        "83": {
            ")": "shift_100"
        },
        "84": {
            "(": "shift_101"
        },
        "85": {
            "while": "reduce_35",
            "endif": "reduce_35",
            "else": "reduce_35",
            "switch": "reduce_35",
            "{": "reduce_35",
            "NUM": "reduce_35",
            "}": "reduce_35",
            "break": "reduce_35",
            "default": "reduce_35",
            "return": "reduce_35",
            "case": "reduce_35",
            "if": "reduce_35",
            "(": "reduce_35",
            ";": "reduce_35",
            "ID": "reduce_35"
        },
        "86": {
            "(": "shift_102"
        },
        "87": {
            ",": "reduce_42",
            "]": "reduce_42",
            ")": "reduce_42",
            ";": "reduce_42"
        },
        "88": {
            ")": "reduce_59",
            "*": "reduce_59",
            "-": "reduce_59",
            ",": "reduce_59",
            "+": "reduce_59",
            "==": "reduce_59",
            "/": "reduce_59",
            "]": "reduce_59",
            ";": "reduce_59",
            "<": "reduce_59"
        },
        "89": {
            "addop": "goto_76",
            "p_operand": "goto_103",
            "+": "reduce_67",
            "/": "reduce_67",
            "*": "reduce_67",
            "-": "reduce_67",
            "<": "reduce_67",
            "==": "reduce_67",
            ",": "reduce_46",
            "]": "reduce_46",
            ")": "reduce_46",
            ";": "reduce_46"
        },
        "90": {
            "mulop": "goto_78",
            "p_operand": "goto_79",
            "+": "reduce_50",
            "/": "reduce_67",
            "*": "reduce_67",
            "-": "reduce_50",
            "<": "reduce_50",
            "==": "reduce_50",
            ")": "reduce_50",
            "]": "reduce_50",
            ",": "reduce_50",
            ";": "reduce_50"
        },
        "91": {
            "NUM": "reduce_48",
            "(": "reduce_48",
            "ID": "reduce_48"
        },
        "92": {
            "NUM": "reduce_49",
            "(": "reduce_49",
            "ID": "reduce_49"
        },
        "93": {
            "NUM": "reduce_52",
            "(": "reduce_52",
            "ID": "reduce_52"
        },
        "94": {
            "NUM": "reduce_53",
            "(": "reduce_53",
            "ID": "reduce_53"
        },
        "95": {
            "+": "reduce_54",
            ")": "reduce_54",
            "*": "reduce_54",
            "-": "reduce_54",
            "==": "reduce_54",
            "/": "reduce_54",
            "]": "reduce_54",
            ",": "reduce_54",
            ";": "reduce_54",
            "<": "reduce_54"
        },
        "96": {
            "NUM": "reduce_56",
            "(": "reduce_56",
            "ID": "reduce_56"
        },
        "97": {
            "NUM": "reduce_57",
            "(": "reduce_57",
            "ID": "reduce_57"
        },
        "98": {
            "(": "shift_42",
            "expression": "goto_104",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "99": {
            "(": "shift_42",
            "expression": "goto_105",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "args": "goto_106",
            "arg_list": "goto_107",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70",
            ")": "reduce_64"
        },
        "100": {
            "save": "goto_108",
            "while": "reduce_74",
            "switch": "reduce_74",
            "{": "reduce_74",
            "NUM": "reduce_74",
            "break": "reduce_74",
            "default": "reduce_74",
            "return": "reduce_74",
            "case": "reduce_74",
            "if": "reduce_74",
            "(": "reduce_74",
            ";": "reduce_74",
            "ID": "reduce_74"
        },
        "101": {
            "(": "shift_42",
            "expression": "goto_109",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "102": {
            "(": "shift_42",
            "expression": "goto_110",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "103": {
            "+": "shift_93",
            "-": "shift_94"
        },
        "104": {
            "]": "shift_111"
        },
        "105": {
            ")": "reduce_66",
            ",": "reduce_66"
        },
        "106": {
            ")": "shift_112"
        },
        "107": {
            ",": "shift_113",
            ")": "reduce_63"
        },
        "108": {
            ";": "shift_41",
            "(": "shift_42",
            "{": "shift_34",
            "break": "shift_44",
            "if": "shift_45",
            "while": "shift_46",
            "return": "shift_47",
            "switch": "shift_48",
            "compound_stmt": "goto_49",
            "statement": "goto_114",
            "expression_stmt": "goto_51",
            "selection_stmt": "goto_52",
            "iteration_stmt": "goto_53",
            "return_stmt": "goto_54",
            "switch_stmt": "goto_55",
            "expression": "goto_56",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "109": {
            ")": "shift_115"
        },
        "110": {
            ")": "shift_116"
        },
        "111": {
            ")": "reduce_45",
            "*": "reduce_45",
            "-": "reduce_45",
            ",": "reduce_45",
            "+": "reduce_45",
            "==": "reduce_45",
            "/": "reduce_45",
            "]": "reduce_45",
            ";": "reduce_45",
            "<": "reduce_45",
            "=": "reduce_45"
        },
        "112": {
            ")": "reduce_62",
            "*": "reduce_62",
            "-": "reduce_62",
            ",": "reduce_62",
            "+": "reduce_62",
            "==": "reduce_62",
            "/": "reduce_62",
            "]": "reduce_62",
            ";": "reduce_62",
            "<": "reduce_62"
        },
        "113": {
            "(": "shift_42",
            "expression": "goto_117",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "114": {
            "endif": "shift_118",
            "else": "shift_119"
        },
        "115": {
            "while_condition": "goto_120",
            "while": "reduce_77",
            "switch": "reduce_77",
            "{": "reduce_77",
            "NUM": "reduce_77",
            "break": "reduce_77",
            "return": "reduce_77",
            "if": "reduce_77",
            "(": "reduce_77",
            ";": "reduce_77",
            "ID": "reduce_77"
        },
        "116": {
            "dummy_save": "goto_121",
            "{": "reduce_79"
        },
        "117": {
            ")": "reduce_65",
            ",": "reduce_65"
        },
        "118": {
            "while": "reduce_31",
            "endif": "reduce_31",
            "else": "reduce_31",
            "switch": "reduce_31",
            "{": "reduce_31",
            "NUM": "reduce_31",
            "}": "reduce_31",
            "break": "reduce_31",
            "default": "reduce_31",
            "return": "reduce_31",
            "case": "reduce_31",
            "if": "reduce_31",
            "(": "reduce_31",
            ";": "reduce_31",
            "ID": "reduce_31"
        },
        "119": {
            "jpf_save": "goto_122",
            "while": "reduce_75",
            "switch": "reduce_75",
            "{": "reduce_75",
            "NUM": "reduce_75",
            "break": "reduce_75",
            "return": "reduce_75",
            "if": "reduce_75",
            "(": "reduce_75",
            ";": "reduce_75",
            "ID": "reduce_75"
        },
        "120": {
            ";": "shift_41",
            "(": "shift_42",
            "{": "shift_34",
            "break": "shift_44",
            "if": "shift_45",
            "while": "shift_46",
            "return": "shift_47",
            "switch": "shift_48",
            "compound_stmt": "goto_49",
            "statement": "goto_123",
            "expression_stmt": "goto_51",
            "selection_stmt": "goto_52",
            "iteration_stmt": "goto_53",
            "return_stmt": "goto_54",
            "switch_stmt": "goto_55",
            "expression": "goto_56",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "121": {
            "{": "shift_124"
        },
        "122": {
            ";": "shift_41",
            "(": "shift_42",
            "{": "shift_34",
            "break": "shift_44",
            "if": "shift_45",
            "while": "shift_46",
            "return": "shift_47",
            "switch": "shift_48",
            "compound_stmt": "goto_49",
            "statement": "goto_125",
            "expression_stmt": "goto_51",
            "selection_stmt": "goto_52",
            "iteration_stmt": "goto_53",
            "return_stmt": "goto_54",
            "switch_stmt": "goto_55",
            "expression": "goto_56",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70"
        },
        "123": {
            "while": "reduce_33",
            "endif": "reduce_33",
            "else": "reduce_33",
            "switch": "reduce_33",
            "{": "reduce_33",
            "NUM": "reduce_33",
            "}": "reduce_33",
            "break": "reduce_33",
            "default": "reduce_33",
            "return": "reduce_33",
            "case": "reduce_33",
            "if": "reduce_33",
            "(": "reduce_33",
            ";": "reduce_33",
            "ID": "reduce_33"
        },
        "124": {
            "case_stmts": "goto_126",
            "case": "reduce_38",
            "default": "reduce_38"
        },
        "125": {
            "endif": "shift_127"
        },
        "126": {
            "case_stmt": "goto_128",
            "default_stmt": "goto_129",
            "jpf": "goto_130",
            "}": "reduce_80",
            "case": "reduce_80",
            "default": "reduce_80"
        },
        "127": {
            "while": "reduce_32",
            "endif": "reduce_32",
            "else": "reduce_32",
            "switch": "reduce_32",
            "{": "reduce_32",
            "NUM": "reduce_32",
            "}": "reduce_32",
            "break": "reduce_32",
            "default": "reduce_32",
            "return": "reduce_32",
            "case": "reduce_32",
            "if": "reduce_32",
            "(": "reduce_32",
            ";": "reduce_32",
            "ID": "reduce_32"
        },
        "128": {
            "case": "reduce_37",
            "default": "reduce_37"
        },
        "129": {
            "}": "shift_131"
        },
        "130": {
            "case": "shift_132",
            "default": "shift_133",
            "}": "reduce_41"
        },
        "131": {
            "while": "reduce_36",
            "endif": "reduce_36",
            "else": "reduce_36",
            "switch": "reduce_36",
            "{": "reduce_36",
            "NUM": "reduce_36",
            "}": "reduce_36",
            "break": "reduce_36",
            "default": "reduce_36",
            "return": "reduce_36",
            "case": "reduce_36",
            "if": "reduce_36",
            "(": "reduce_36",
            ";": "reduce_36",
            "ID": "reduce_36"
        },
        "132": {
            "case_condition": "goto_134",
            "NUM": "reduce_78"
        },
        "133": {
            ":": "shift_135"
        },
        "134": {
            "NUM": "shift_136"
        },
        "135": {
            "statement_list": "goto_137",
            "while": "reduce_21",
            "switch": "reduce_21",
            "{": "reduce_21",
            "NUM": "reduce_21",
            "}": "reduce_21",
            "break": "reduce_21",
            "default": "reduce_21",
            "return": "reduce_21",
            "case": "reduce_21",
            "if": "reduce_21",
            "(": "reduce_21",
            ";": "reduce_21",
            "ID": "reduce_21"
        },
        "136": {
            ":": "shift_138"
        },
        "137": {
            ";": "shift_41",
            "(": "shift_42",
            "{": "shift_34",
            "break": "shift_44",
            "if": "shift_45",
            "while": "shift_46",
            "return": "shift_47",
            "switch": "shift_48",
            "compound_stmt": "goto_49",
            "statement": "goto_50",
            "expression_stmt": "goto_51",
            "selection_stmt": "goto_52",
            "iteration_stmt": "goto_53",
            "return_stmt": "goto_54",
            "switch_stmt": "goto_55",
            "expression": "goto_56",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70",
            "}": "reduce_40"
        },
        "138": {
            "save": "goto_139",
            "while": "reduce_74",
            "switch": "reduce_74",
            "{": "reduce_74",
            "NUM": "reduce_74",
            "break": "reduce_74",
            "default": "reduce_74",
            "return": "reduce_74",
            "case": "reduce_74",
            "if": "reduce_74",
            "(": "reduce_74",
            ";": "reduce_74",
            "ID": "reduce_74"
        },
        "139": {
            "statement_list": "goto_140",
            "while": "reduce_21",
            "switch": "reduce_21",
            "{": "reduce_21",
            "NUM": "reduce_21",
            "}": "reduce_21",
            "break": "reduce_21",
            "default": "reduce_21",
            "return": "reduce_21",
            "case": "reduce_21",
            "if": "reduce_21",
            "(": "reduce_21",
            ";": "reduce_21",
            "ID": "reduce_21"
        },
        "140": {
            ";": "shift_41",
            "(": "shift_42",
            "{": "shift_34",
            "break": "shift_44",
            "if": "shift_45",
            "while": "shift_46",
            "return": "shift_47",
            "switch": "shift_48",
            "compound_stmt": "goto_49",
            "statement": "goto_50",
            "expression_stmt": "goto_51",
            "selection_stmt": "goto_52",
            "iteration_stmt": "goto_53",
            "return_stmt": "goto_54",
            "switch_stmt": "goto_55",
            "expression": "goto_56",
            "var": "goto_57",
            "simple_expression": "goto_58",
            "additive_expression": "goto_59",
            "term": "goto_60",
            "factor": "goto_61",
            "call": "goto_62",
            "p_id": "goto_63",
            "p_num_temp": "goto_64",
            "NUM": "reduce_73",
            "ID": "reduce_70",
            "case": "reduce_39",
            "default": "reduce_39"
        }
    }
}