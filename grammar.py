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
        "p_id_index",
        "p_num",
        "p_label",
        "p_id",
        "p_num_temp",
        "func_declare",
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
            "NUM",
            "{",
            "while",
            "if",
            "(",
            "break",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "statement": [
            "NUM",
            "(",
            "{",
            "break",
            "while",
            "if",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "expression_stmt": [
            "ID",
            "NUM",
            "(",
            ";",
            "break"
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
            "ID",
            "NUM",
            "("
        ],
        "var": [
            "ID"
        ],
        "simple_expression": [
            "ID",
            "NUM",
            "("
        ],
        "relop": [
            "<",
            "=="
        ],
        "additive_expression": [
            "ID",
            "NUM",
            "("
        ],
        "addop": [
            "+",
            "-"
        ],
        "term": [
            "ID",
            "NUM",
            "("
        ],
        "mulop": [
            "/",
            "*"
        ],
        "factor": [
            "ID",
            "NUM",
            "("
        ],
        "call": [
            "ID"
        ],
        "args": [
            "ID",
            "NUM",
            "("
        ],
        "arg_list": [
            "ID",
            "NUM",
            "("
        ],
        "p_id_index": [],
        "p_num": [],
        "p_label": [],
        "p_id": [],
        "p_num_temp": [],
        "func_declare": [],
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
            "$",
            "int"
        ],
        "declaration": [
            "void",
            "$",
            "int"
        ],
        "var_declaration": [
            "NUM",
            "{",
            "}",
            "int",
            "while",
            "if",
            "void",
            "(",
            "break",
            "ID",
            "$",
            "return",
            "switch",
            ";"
        ],
        "type_specifier": [
            "ID"
        ],
        "fun_declaration": [
            "void",
            "$",
            "int"
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
            "NUM",
            "}",
            "{",
            "int",
            "while",
            "if",
            "endif",
            "void",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "$",
            "return",
            "switch",
            ";",
            "else"
        ],
        "local_declarations": [
            "NUM",
            "{",
            "}",
            "int",
            "while",
            "if",
            "void",
            "(",
            "break",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "statement_list": [
            "NUM",
            "{",
            "}",
            "while",
            "if",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "statement": [
            "NUM",
            "}",
            "{",
            "while",
            "if",
            "endif",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";",
            "else"
        ],
        "expression_stmt": [
            "NUM",
            "}",
            "{",
            "while",
            "if",
            "endif",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";",
            "else"
        ],
        "selection_stmt": [
            "NUM",
            "}",
            "{",
            "while",
            "if",
            "endif",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";",
            "else"
        ],
        "iteration_stmt": [
            "NUM",
            "}",
            "{",
            "while",
            "if",
            "endif",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";",
            "else"
        ],
        "return_stmt": [
            "NUM",
            "}",
            "{",
            "while",
            "if",
            "endif",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";",
            "else"
        ],
        "switch_stmt": [
            "NUM",
            "}",
            "{",
            "while",
            "if",
            "endif",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";",
            "else"
        ],
        "case_stmts": [
            "default",
            "case"
        ],
        "case_stmt": [
            "default",
            "case"
        ],
        "default_stmt": [
            "}"
        ],
        "expression": [
            ")",
            ";",
            ",",
            "]"
        ],
        "var": [
            "==",
            ")",
            "]",
            "<",
            "/",
            "*",
            "+",
            "=",
            ",",
            ";",
            "-"
        ],
        "simple_expression": [
            ")",
            ";",
            ",",
            "]"
        ],
        "relop": [
            "ID",
            "NUM",
            "("
        ],
        "additive_expression": [
            "+",
            "==",
            ")",
            ",",
            "]",
            "<",
            ";",
            "-"
        ],
        "addop": [
            "ID",
            "NUM",
            "("
        ],
        "term": [
            "+",
            "==",
            ")",
            ",",
            "]",
            "<",
            "/",
            ";",
            "-",
            "*"
        ],
        "mulop": [
            "ID",
            "NUM",
            "("
        ],
        "factor": [
            "==",
            ")",
            "]",
            "<",
            "/",
            "*",
            "+",
            ",",
            ";",
            "-"
        ],
        "call": [
            "==",
            ")",
            "]",
            "<",
            "/",
            "*",
            "+",
            ",",
            ";",
            "-"
        ],
        "args": [
            ")"
        ],
        "arg_list": [
            ")",
            ","
        ],
        "p_id_index": [
            "ID"
        ],
        "p_num": [
            "NUM"
        ],
        "p_label": [
            "+",
            "void",
            "==",
            "int",
            "<",
            "/",
            "-",
            "*"
        ],
        "p_id": [
            "ID"
        ],
        "p_num_temp": [
            "NUM"
        ],
        "func_declare": [
            "("
        ],
        "save": [
            "NUM",
            "{",
            "while",
            "if",
            "(",
            "break",
            "default",
            "case",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "jpf_save": [
            "NUM",
            "{",
            "while",
            "if",
            "(",
            "break",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "save_break_temp": [
            "("
        ],
        "while_condition": [
            "NUM",
            "{",
            "while",
            "if",
            "(",
            "break",
            "ID",
            "return",
            "switch",
            ";"
        ],
        "case_condition": [
            "NUM"
        ],
        "dummy_save": [
            "{"
        ],
        "jpf": [
            "default",
            "case",
            "}"
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
            "p_id_index",
            "ID",
            ";"
        ],
        "7": [
            "var_declaration",
            "->",
            "type_specifier",
            "p_id_index",
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
            "p_label",
            "int"
        ],
        "9": [
            "type_specifier",
            "->",
            "p_label",
            "void"
        ],
        "10": [
            "fun_declaration",
            "->",
            "type_specifier",
            "p_id_index",
            "ID",
            "func_declare",
            "(",
            "params",
            ")",
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
            "p_label",
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
            "p_id_index",
            "ID"
        ],
        "16": [
            "param",
            "->",
            "type_specifier",
            "p_id_index",
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
            "p_label",
            "<"
        ],
        "49": [
            "relop",
            "->",
            "p_label",
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
            "p_label",
            "+"
        ],
        "53": [
            "addop",
            "->",
            "p_label",
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
            "p_label",
            "*"
        ],
        "57": [
            "mulop",
            "->",
            "p_label",
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
            "p_id_index",
            "->",
            "epsilon"
        ],
        "68": [
            "p_num",
            "->",
            "epsilon"
        ],
        "69": [
            "p_label",
            "->",
            "epsilon"
        ],
        "70": [
            "p_id",
            "->",
            "epsilon"
        ],
        "71": [
            "p_num_temp",
            "->",
            "epsilon"
        ],
        "72": [
            "func_declare",
            "->",
            "epsilon"
        ],
        "73": [
            "save",
            "->",
            "epsilon"
        ],
        "74": [
            "jpf_save",
            "->",
            "epsilon"
        ],
        "75": [
            "save_break_temp",
            "->",
            "epsilon"
        ],
        "76": [
            "while_condition",
            "->",
            "epsilon"
        ],
        "77": [
            "case_condition",
            "->",
            "epsilon"
        ],
        "78": [
            "dummy_save",
            "->",
            "epsilon"
        ],
        "79": [
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
            "p_label": "goto_7",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69"
        },
        "1": {
            "$": "shift_8"
        },
        "2": {
            "declaration": "goto_9",
            "var_declaration": "goto_4",
            "type_specifier": "goto_5",
            "fun_declaration": "goto_6",
            "p_label": "goto_7",
            "$": "reduce_1",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69"
        },
        "3": {
            "void": "reduce_3",
            "$": "reduce_3",
            "int": "reduce_3"
        },
        "4": {
            "void": "reduce_4",
            "$": "reduce_4",
            "int": "reduce_4"
        },
        "5": {
            "p_id_index": "goto_10",
            "ID": "reduce_67"
        },
        "6": {
            "void": "reduce_5",
            "$": "reduce_5",
            "int": "reduce_5"
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
            "$": "reduce_2",
            "int": "reduce_2"
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
            "func_declare": "goto_16",
            "(": "reduce_72"
        },
        "14": {
            "NUM": "reduce_6",
            "{": "reduce_6",
            "}": "reduce_6",
            "int": "reduce_6",
            "while": "reduce_6",
            "if": "reduce_6",
            "void": "reduce_6",
            "(": "reduce_6",
            "break": "reduce_6",
            "ID": "reduce_6",
            "$": "reduce_6",
            "return": "reduce_6",
            "switch": "reduce_6",
            ";": "reduce_6"
        },
        "15": {
            "p_num": "goto_17",
            "NUM": "reduce_68"
        },
        "16": {
            "(": "shift_18"
        },
        "17": {
            "NUM": "shift_19"
        },
        "18": {
            "type_specifier": "goto_20",
            "params": "goto_21",
            "param_list": "goto_22",
            "param": "goto_23",
            "p_label": "goto_24",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69"
        },
        "19": {
            "]": "shift_25"
        },
        "20": {
            "p_id_index": "goto_26",
            "ID": "reduce_67"
        },
        "21": {
            ")": "shift_27"
        },
        "22": {
            ",": "shift_28",
            ")": "reduce_11"
        },
        "23": {
            ")": "reduce_14",
            ",": "reduce_14"
        },
        "24": {
            "int": "shift_11",
            "void": "shift_29"
        },
        "25": {
            ";": "shift_30"
        },
        "26": {
            "ID": "shift_31"
        },
        "27": {
            "{": "shift_32",
            "compound_stmt": "goto_33"
        },
        "28": {
            "type_specifier": "goto_20",
            "param": "goto_34",
            "p_label": "goto_7",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69"
        },
        "29": {
            ")": "reduce_12",
            "ID": "reduce_9"
        },
        "30": {
            "NUM": "reduce_7",
            "{": "reduce_7",
            "}": "reduce_7",
            "int": "reduce_7",
            "while": "reduce_7",
            "if": "reduce_7",
            "void": "reduce_7",
            "(": "reduce_7",
            "break": "reduce_7",
            "ID": "reduce_7",
            "$": "reduce_7",
            "return": "reduce_7",
            "switch": "reduce_7",
            ";": "reduce_7"
        },
        "31": {
            "[": "shift_35",
            ")": "reduce_15",
            ",": "reduce_15"
        },
        "32": {
            "local_declarations": "goto_36",
            "NUM": "reduce_19",
            "{": "reduce_19",
            "}": "reduce_19",
            "int": "reduce_19",
            "while": "reduce_19",
            "if": "reduce_19",
            "void": "reduce_19",
            "(": "reduce_19",
            "break": "reduce_19",
            "ID": "reduce_19",
            "return": "reduce_19",
            "switch": "reduce_19",
            ";": "reduce_19"
        },
        "33": {
            "void": "reduce_10",
            "$": "reduce_10",
            "int": "reduce_10"
        },
        "34": {
            ")": "reduce_13",
            ",": "reduce_13"
        },
        "35": {
            "]": "shift_37"
        },
        "36": {
            "var_declaration": "goto_38",
            "type_specifier": "goto_39",
            "statement_list": "goto_40",
            "p_label": "goto_7",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69",
            "NUM": "reduce_21",
            "{": "reduce_21",
            "}": "reduce_21",
            "while": "reduce_21",
            "if": "reduce_21",
            "(": "reduce_21",
            "break": "reduce_21",
            "default": "reduce_21",
            "case": "reduce_21",
            "ID": "reduce_21",
            "return": "reduce_21",
            "switch": "reduce_21",
            ";": "reduce_21"
        },
        "37": {
            ")": "reduce_16",
            ",": "reduce_16"
        },
        "38": {
            "NUM": "reduce_18",
            "{": "reduce_18",
            "}": "reduce_18",
            "int": "reduce_18",
            "while": "reduce_18",
            "if": "reduce_18",
            "void": "reduce_18",
            "(": "reduce_18",
            "break": "reduce_18",
            "ID": "reduce_18",
            "return": "reduce_18",
            "switch": "reduce_18",
            ";": "reduce_18"
        },
        "39": {
            "p_id_index": "goto_41",
            "ID": "reduce_67"
        },
        "40": {
            ";": "shift_42",
            "(": "shift_43",
            "{": "shift_32",
            "}": "shift_44",
            "break": "shift_45",
            "if": "shift_46",
            "while": "shift_47",
            "return": "shift_48",
            "switch": "shift_49",
            "compound_stmt": "goto_50",
            "statement": "goto_51",
            "expression_stmt": "goto_52",
            "selection_stmt": "goto_53",
            "iteration_stmt": "goto_54",
            "return_stmt": "goto_55",
            "switch_stmt": "goto_56",
            "expression": "goto_57",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "41": {
            "ID": "shift_66"
        },
        "42": {
            "NUM": "reduce_30",
            "}": "reduce_30",
            "{": "reduce_30",
            "while": "reduce_30",
            "if": "reduce_30",
            "endif": "reduce_30",
            "(": "reduce_30",
            "break": "reduce_30",
            "default": "reduce_30",
            "case": "reduce_30",
            "ID": "reduce_30",
            "return": "reduce_30",
            "switch": "reduce_30",
            ";": "reduce_30",
            "else": "reduce_30"
        },
        "43": {
            "(": "shift_43",
            "expression": "goto_67",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "44": {
            "NUM": "reduce_17",
            "}": "reduce_17",
            "{": "reduce_17",
            "int": "reduce_17",
            "while": "reduce_17",
            "if": "reduce_17",
            "endif": "reduce_17",
            "void": "reduce_17",
            "(": "reduce_17",
            "break": "reduce_17",
            "default": "reduce_17",
            "case": "reduce_17",
            "ID": "reduce_17",
            "$": "reduce_17",
            "return": "reduce_17",
            "switch": "reduce_17",
            ";": "reduce_17",
            "else": "reduce_17"
        },
        "45": {
            ";": "shift_68"
        },
        "46": {
            "(": "shift_69"
        },
        "47": {
            "save": "goto_70",
            "NUM": "reduce_73",
            "{": "reduce_73",
            "while": "reduce_73",
            "if": "reduce_73",
            "(": "reduce_73",
            "break": "reduce_73",
            "default": "reduce_73",
            "case": "reduce_73",
            "ID": "reduce_73",
            "return": "reduce_73",
            "switch": "reduce_73",
            ";": "reduce_73"
        },
        "48": {
            ";": "shift_71",
            "(": "shift_43",
            "expression": "goto_72",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "49": {
            "save": "goto_73",
            "NUM": "reduce_73",
            "{": "reduce_73",
            "while": "reduce_73",
            "if": "reduce_73",
            "(": "reduce_73",
            "break": "reduce_73",
            "default": "reduce_73",
            "case": "reduce_73",
            "ID": "reduce_73",
            "return": "reduce_73",
            "switch": "reduce_73",
            ";": "reduce_73"
        },
        "50": {
            "NUM": "reduce_23",
            "}": "reduce_23",
            "{": "reduce_23",
            "while": "reduce_23",
            "if": "reduce_23",
            "endif": "reduce_23",
            "(": "reduce_23",
            "break": "reduce_23",
            "default": "reduce_23",
            "case": "reduce_23",
            "ID": "reduce_23",
            "return": "reduce_23",
            "switch": "reduce_23",
            ";": "reduce_23",
            "else": "reduce_23"
        },
        "51": {
            "NUM": "reduce_20",
            "{": "reduce_20",
            "}": "reduce_20",
            "while": "reduce_20",
            "if": "reduce_20",
            "(": "reduce_20",
            "break": "reduce_20",
            "default": "reduce_20",
            "case": "reduce_20",
            "ID": "reduce_20",
            "return": "reduce_20",
            "switch": "reduce_20",
            ";": "reduce_20"
        },
        "52": {
            "NUM": "reduce_22",
            "}": "reduce_22",
            "{": "reduce_22",
            "while": "reduce_22",
            "if": "reduce_22",
            "endif": "reduce_22",
            "(": "reduce_22",
            "break": "reduce_22",
            "default": "reduce_22",
            "case": "reduce_22",
            "ID": "reduce_22",
            "return": "reduce_22",
            "switch": "reduce_22",
            ";": "reduce_22",
            "else": "reduce_22"
        },
        "53": {
            "NUM": "reduce_24",
            "}": "reduce_24",
            "{": "reduce_24",
            "while": "reduce_24",
            "if": "reduce_24",
            "endif": "reduce_24",
            "(": "reduce_24",
            "break": "reduce_24",
            "default": "reduce_24",
            "case": "reduce_24",
            "ID": "reduce_24",
            "return": "reduce_24",
            "switch": "reduce_24",
            ";": "reduce_24",
            "else": "reduce_24"
        },
        "54": {
            "NUM": "reduce_25",
            "}": "reduce_25",
            "{": "reduce_25",
            "while": "reduce_25",
            "if": "reduce_25",
            "endif": "reduce_25",
            "(": "reduce_25",
            "break": "reduce_25",
            "default": "reduce_25",
            "case": "reduce_25",
            "ID": "reduce_25",
            "return": "reduce_25",
            "switch": "reduce_25",
            ";": "reduce_25",
            "else": "reduce_25"
        },
        "55": {
            "NUM": "reduce_26",
            "}": "reduce_26",
            "{": "reduce_26",
            "while": "reduce_26",
            "if": "reduce_26",
            "endif": "reduce_26",
            "(": "reduce_26",
            "break": "reduce_26",
            "default": "reduce_26",
            "case": "reduce_26",
            "ID": "reduce_26",
            "return": "reduce_26",
            "switch": "reduce_26",
            ";": "reduce_26",
            "else": "reduce_26"
        },
        "56": {
            "NUM": "reduce_27",
            "}": "reduce_27",
            "{": "reduce_27",
            "while": "reduce_27",
            "if": "reduce_27",
            "endif": "reduce_27",
            "(": "reduce_27",
            "break": "reduce_27",
            "default": "reduce_27",
            "case": "reduce_27",
            "ID": "reduce_27",
            "return": "reduce_27",
            "switch": "reduce_27",
            ";": "reduce_27",
            "else": "reduce_27"
        },
        "57": {
            ";": "shift_74"
        },
        "58": {
            "=": "shift_75",
            "==": "reduce_59",
            ")": "reduce_59",
            "]": "reduce_59",
            "<": "reduce_59",
            "/": "reduce_59",
            "*": "reduce_59",
            "+": "reduce_59",
            ",": "reduce_59",
            ";": "reduce_59",
            "-": "reduce_59"
        },
        "59": {
            ")": "reduce_43",
            ";": "reduce_43",
            ",": "reduce_43",
            "]": "reduce_43"
        },
        "60": {
            "relop": "goto_76",
            "addop": "goto_77",
            "p_label": "goto_78",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69",
            ")": "reduce_47",
            ";": "reduce_47",
            ",": "reduce_47",
            "]": "reduce_47"
        },
        "61": {
            "mulop": "goto_79",
            "p_label": "goto_80",
            "+": "reduce_51",
            "void": "reduce_69",
            "==": "reduce_51",
            "int": "reduce_69",
            "<": "reduce_51",
            "/": "reduce_69",
            "-": "reduce_51",
            "*": "reduce_69",
            ")": "reduce_51",
            ",": "reduce_51",
            "]": "reduce_51",
            ";": "reduce_51"
        },
        "62": {
            "+": "reduce_55",
            "==": "reduce_55",
            ")": "reduce_55",
            ",": "reduce_55",
            "]": "reduce_55",
            "<": "reduce_55",
            "/": "reduce_55",
            ";": "reduce_55",
            "-": "reduce_55",
            "*": "reduce_55"
        },
        "63": {
            "==": "reduce_60",
            ")": "reduce_60",
            "]": "reduce_60",
            "<": "reduce_60",
            "/": "reduce_60",
            "*": "reduce_60",
            "+": "reduce_60",
            ",": "reduce_60",
            ";": "reduce_60",
            "-": "reduce_60"
        },
        "64": {
            "ID": "shift_81"
        },
        "65": {
            "NUM": "shift_82"
        },
        "66": {
            ";": "shift_14",
            "[": "shift_15"
        },
        "67": {
            ")": "shift_83"
        },
        "68": {
            "NUM": "reduce_29",
            "}": "reduce_29",
            "{": "reduce_29",
            "while": "reduce_29",
            "if": "reduce_29",
            "endif": "reduce_29",
            "(": "reduce_29",
            "break": "reduce_29",
            "default": "reduce_29",
            "case": "reduce_29",
            "ID": "reduce_29",
            "return": "reduce_29",
            "switch": "reduce_29",
            ";": "reduce_29",
            "else": "reduce_29"
        },
        "69": {
            "(": "shift_43",
            "expression": "goto_84",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "70": {
            "save_break_temp": "goto_85",
            "(": "reduce_75"
        },
        "71": {
            "NUM": "reduce_34",
            "}": "reduce_34",
            "{": "reduce_34",
            "while": "reduce_34",
            "if": "reduce_34",
            "endif": "reduce_34",
            "(": "reduce_34",
            "break": "reduce_34",
            "default": "reduce_34",
            "case": "reduce_34",
            "ID": "reduce_34",
            "return": "reduce_34",
            "switch": "reduce_34",
            ";": "reduce_34",
            "else": "reduce_34"
        },
        "72": {
            ";": "shift_86"
        },
        "73": {
            "save_break_temp": "goto_87",
            "(": "reduce_75"
        },
        "74": {
            "NUM": "reduce_28",
            "}": "reduce_28",
            "{": "reduce_28",
            "while": "reduce_28",
            "if": "reduce_28",
            "endif": "reduce_28",
            "(": "reduce_28",
            "break": "reduce_28",
            "default": "reduce_28",
            "case": "reduce_28",
            "ID": "reduce_28",
            "return": "reduce_28",
            "switch": "reduce_28",
            ";": "reduce_28",
            "else": "reduce_28"
        },
        "75": {
            "(": "shift_43",
            "expression": "goto_88",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "76": {
            "(": "shift_43",
            "var": "goto_89",
            "additive_expression": "goto_90",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "77": {
            "(": "shift_43",
            "var": "goto_89",
            "term": "goto_91",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "78": {
            "<": "shift_92",
            "==": "shift_93",
            "+": "shift_94",
            "-": "shift_95"
        },
        "79": {
            "(": "shift_43",
            "var": "goto_89",
            "factor": "goto_96",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "80": {
            "*": "shift_97",
            "/": "shift_98"
        },
        "81": {
            "[": "shift_99",
            "(": "shift_100",
            "==": "reduce_44",
            ")": "reduce_44",
            "]": "reduce_44",
            "<": "reduce_44",
            "/": "reduce_44",
            "*": "reduce_44",
            "+": "reduce_44",
            "=": "reduce_44",
            ",": "reduce_44",
            ";": "reduce_44",
            "-": "reduce_44"
        },
        "82": {
            "==": "reduce_61",
            ")": "reduce_61",
            "]": "reduce_61",
            "<": "reduce_61",
            "/": "reduce_61",
            "*": "reduce_61",
            "+": "reduce_61",
            ",": "reduce_61",
            ";": "reduce_61",
            "-": "reduce_61"
        },
        "83": {
            "==": "reduce_58",
            ")": "reduce_58",
            "]": "reduce_58",
            "<": "reduce_58",
            "/": "reduce_58",
            "*": "reduce_58",
            "+": "reduce_58",
            ",": "reduce_58",
            ";": "reduce_58",
            "-": "reduce_58"
        },
        "84": {
            ")": "shift_101"
        },
        "85": {
            "(": "shift_102"
        },
        "86": {
            "NUM": "reduce_35",
            "}": "reduce_35",
            "{": "reduce_35",
            "while": "reduce_35",
            "if": "reduce_35",
            "endif": "reduce_35",
            "(": "reduce_35",
            "break": "reduce_35",
            "default": "reduce_35",
            "case": "reduce_35",
            "ID": "reduce_35",
            "return": "reduce_35",
            "switch": "reduce_35",
            ";": "reduce_35",
            "else": "reduce_35"
        },
        "87": {
            "(": "shift_103"
        },
        "88": {
            ")": "reduce_42",
            ";": "reduce_42",
            ",": "reduce_42",
            "]": "reduce_42"
        },
        "89": {
            "==": "reduce_59",
            ")": "reduce_59",
            "]": "reduce_59",
            "<": "reduce_59",
            "/": "reduce_59",
            "*": "reduce_59",
            "+": "reduce_59",
            ",": "reduce_59",
            ";": "reduce_59",
            "-": "reduce_59"
        },
        "90": {
            "addop": "goto_77",
            "p_label": "goto_104",
            "+": "reduce_69",
            "void": "reduce_69",
            "==": "reduce_69",
            "int": "reduce_69",
            "<": "reduce_69",
            "/": "reduce_69",
            "-": "reduce_69",
            "*": "reduce_69",
            ")": "reduce_46",
            ";": "reduce_46",
            ",": "reduce_46",
            "]": "reduce_46"
        },
        "91": {
            "mulop": "goto_79",
            "p_label": "goto_80",
            "+": "reduce_50",
            "void": "reduce_69",
            "==": "reduce_50",
            "int": "reduce_69",
            "<": "reduce_50",
            "/": "reduce_69",
            "-": "reduce_50",
            "*": "reduce_69",
            ")": "reduce_50",
            ",": "reduce_50",
            "]": "reduce_50",
            ";": "reduce_50"
        },
        "92": {
            "ID": "reduce_48",
            "NUM": "reduce_48",
            "(": "reduce_48"
        },
        "93": {
            "ID": "reduce_49",
            "NUM": "reduce_49",
            "(": "reduce_49"
        },
        "94": {
            "ID": "reduce_52",
            "NUM": "reduce_52",
            "(": "reduce_52"
        },
        "95": {
            "ID": "reduce_53",
            "NUM": "reduce_53",
            "(": "reduce_53"
        },
        "96": {
            "+": "reduce_54",
            "==": "reduce_54",
            ")": "reduce_54",
            ",": "reduce_54",
            "]": "reduce_54",
            "<": "reduce_54",
            "/": "reduce_54",
            ";": "reduce_54",
            "-": "reduce_54",
            "*": "reduce_54"
        },
        "97": {
            "ID": "reduce_56",
            "NUM": "reduce_56",
            "(": "reduce_56"
        },
        "98": {
            "ID": "reduce_57",
            "NUM": "reduce_57",
            "(": "reduce_57"
        },
        "99": {
            "(": "shift_43",
            "expression": "goto_105",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "100": {
            "(": "shift_43",
            "expression": "goto_106",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "args": "goto_107",
            "arg_list": "goto_108",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70",
            ")": "reduce_64"
        },
        "101": {
            "save": "goto_109",
            "NUM": "reduce_73",
            "{": "reduce_73",
            "while": "reduce_73",
            "if": "reduce_73",
            "(": "reduce_73",
            "break": "reduce_73",
            "default": "reduce_73",
            "case": "reduce_73",
            "ID": "reduce_73",
            "return": "reduce_73",
            "switch": "reduce_73",
            ";": "reduce_73"
        },
        "102": {
            "(": "shift_43",
            "expression": "goto_110",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "103": {
            "(": "shift_43",
            "expression": "goto_111",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "104": {
            "+": "shift_94",
            "-": "shift_95"
        },
        "105": {
            "]": "shift_112"
        },
        "106": {
            ")": "reduce_66",
            ",": "reduce_66"
        },
        "107": {
            ")": "shift_113"
        },
        "108": {
            ",": "shift_114",
            ")": "reduce_63"
        },
        "109": {
            ";": "shift_42",
            "(": "shift_43",
            "{": "shift_32",
            "break": "shift_45",
            "if": "shift_46",
            "while": "shift_47",
            "return": "shift_48",
            "switch": "shift_49",
            "compound_stmt": "goto_50",
            "statement": "goto_115",
            "expression_stmt": "goto_52",
            "selection_stmt": "goto_53",
            "iteration_stmt": "goto_54",
            "return_stmt": "goto_55",
            "switch_stmt": "goto_56",
            "expression": "goto_57",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "110": {
            ")": "shift_116"
        },
        "111": {
            ")": "shift_117"
        },
        "112": {
            "==": "reduce_45",
            ")": "reduce_45",
            "]": "reduce_45",
            "<": "reduce_45",
            "/": "reduce_45",
            "*": "reduce_45",
            "+": "reduce_45",
            "=": "reduce_45",
            ",": "reduce_45",
            ";": "reduce_45",
            "-": "reduce_45"
        },
        "113": {
            "==": "reduce_62",
            ")": "reduce_62",
            "]": "reduce_62",
            "<": "reduce_62",
            "/": "reduce_62",
            "*": "reduce_62",
            "+": "reduce_62",
            ",": "reduce_62",
            ";": "reduce_62",
            "-": "reduce_62"
        },
        "114": {
            "(": "shift_43",
            "expression": "goto_118",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "115": {
            "endif": "shift_119",
            "else": "shift_120"
        },
        "116": {
            "while_condition": "goto_121",
            "NUM": "reduce_76",
            "{": "reduce_76",
            "while": "reduce_76",
            "if": "reduce_76",
            "(": "reduce_76",
            "break": "reduce_76",
            "ID": "reduce_76",
            "return": "reduce_76",
            "switch": "reduce_76",
            ";": "reduce_76"
        },
        "117": {
            "dummy_save": "goto_122",
            "{": "reduce_78"
        },
        "118": {
            ")": "reduce_65",
            ",": "reduce_65"
        },
        "119": {
            "NUM": "reduce_31",
            "}": "reduce_31",
            "{": "reduce_31",
            "while": "reduce_31",
            "if": "reduce_31",
            "endif": "reduce_31",
            "(": "reduce_31",
            "break": "reduce_31",
            "default": "reduce_31",
            "case": "reduce_31",
            "ID": "reduce_31",
            "return": "reduce_31",
            "switch": "reduce_31",
            ";": "reduce_31",
            "else": "reduce_31"
        },
        "120": {
            "jpf_save": "goto_123",
            "NUM": "reduce_74",
            "{": "reduce_74",
            "while": "reduce_74",
            "if": "reduce_74",
            "(": "reduce_74",
            "break": "reduce_74",
            "ID": "reduce_74",
            "return": "reduce_74",
            "switch": "reduce_74",
            ";": "reduce_74"
        },
        "121": {
            ";": "shift_42",
            "(": "shift_43",
            "{": "shift_32",
            "break": "shift_45",
            "if": "shift_46",
            "while": "shift_47",
            "return": "shift_48",
            "switch": "shift_49",
            "compound_stmt": "goto_50",
            "statement": "goto_124",
            "expression_stmt": "goto_52",
            "selection_stmt": "goto_53",
            "iteration_stmt": "goto_54",
            "return_stmt": "goto_55",
            "switch_stmt": "goto_56",
            "expression": "goto_57",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "122": {
            "{": "shift_125"
        },
        "123": {
            ";": "shift_42",
            "(": "shift_43",
            "{": "shift_32",
            "break": "shift_45",
            "if": "shift_46",
            "while": "shift_47",
            "return": "shift_48",
            "switch": "shift_49",
            "compound_stmt": "goto_50",
            "statement": "goto_126",
            "expression_stmt": "goto_52",
            "selection_stmt": "goto_53",
            "iteration_stmt": "goto_54",
            "return_stmt": "goto_55",
            "switch_stmt": "goto_56",
            "expression": "goto_57",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70"
        },
        "124": {
            "NUM": "reduce_33",
            "}": "reduce_33",
            "{": "reduce_33",
            "while": "reduce_33",
            "if": "reduce_33",
            "endif": "reduce_33",
            "(": "reduce_33",
            "break": "reduce_33",
            "default": "reduce_33",
            "case": "reduce_33",
            "ID": "reduce_33",
            "return": "reduce_33",
            "switch": "reduce_33",
            ";": "reduce_33",
            "else": "reduce_33"
        },
        "125": {
            "case_stmts": "goto_127",
            "default": "reduce_38",
            "case": "reduce_38"
        },
        "126": {
            "endif": "shift_128"
        },
        "127": {
            "case_stmt": "goto_129",
            "default_stmt": "goto_130",
            "jpf": "goto_131",
            "default": "reduce_79",
            "case": "reduce_79",
            "}": "reduce_79"
        },
        "128": {
            "NUM": "reduce_32",
            "}": "reduce_32",
            "{": "reduce_32",
            "while": "reduce_32",
            "if": "reduce_32",
            "endif": "reduce_32",
            "(": "reduce_32",
            "break": "reduce_32",
            "default": "reduce_32",
            "case": "reduce_32",
            "ID": "reduce_32",
            "return": "reduce_32",
            "switch": "reduce_32",
            ";": "reduce_32",
            "else": "reduce_32"
        },
        "129": {
            "default": "reduce_37",
            "case": "reduce_37"
        },
        "130": {
            "}": "shift_132"
        },
        "131": {
            "case": "shift_133",
            "default": "shift_134",
            "}": "reduce_41"
        },
        "132": {
            "NUM": "reduce_36",
            "}": "reduce_36",
            "{": "reduce_36",
            "while": "reduce_36",
            "if": "reduce_36",
            "endif": "reduce_36",
            "(": "reduce_36",
            "break": "reduce_36",
            "default": "reduce_36",
            "case": "reduce_36",
            "ID": "reduce_36",
            "return": "reduce_36",
            "switch": "reduce_36",
            ";": "reduce_36",
            "else": "reduce_36"
        },
        "133": {
            "case_condition": "goto_135",
            "NUM": "reduce_77"
        },
        "134": {
            ":": "shift_136"
        },
        "135": {
            "NUM": "shift_137"
        },
        "136": {
            "statement_list": "goto_138",
            "NUM": "reduce_21",
            "{": "reduce_21",
            "}": "reduce_21",
            "while": "reduce_21",
            "if": "reduce_21",
            "(": "reduce_21",
            "break": "reduce_21",
            "default": "reduce_21",
            "case": "reduce_21",
            "ID": "reduce_21",
            "return": "reduce_21",
            "switch": "reduce_21",
            ";": "reduce_21"
        },
        "137": {
            ":": "shift_139"
        },
        "138": {
            ";": "shift_42",
            "(": "shift_43",
            "{": "shift_32",
            "break": "shift_45",
            "if": "shift_46",
            "while": "shift_47",
            "return": "shift_48",
            "switch": "shift_49",
            "compound_stmt": "goto_50",
            "statement": "goto_51",
            "expression_stmt": "goto_52",
            "selection_stmt": "goto_53",
            "iteration_stmt": "goto_54",
            "return_stmt": "goto_55",
            "switch_stmt": "goto_56",
            "expression": "goto_57",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70",
            "}": "reduce_40"
        },
        "139": {
            "save": "goto_140",
            "NUM": "reduce_73",
            "{": "reduce_73",
            "while": "reduce_73",
            "if": "reduce_73",
            "(": "reduce_73",
            "break": "reduce_73",
            "default": "reduce_73",
            "case": "reduce_73",
            "ID": "reduce_73",
            "return": "reduce_73",
            "switch": "reduce_73",
            ";": "reduce_73"
        },
        "140": {
            "statement_list": "goto_141",
            "NUM": "reduce_21",
            "{": "reduce_21",
            "}": "reduce_21",
            "while": "reduce_21",
            "if": "reduce_21",
            "(": "reduce_21",
            "break": "reduce_21",
            "default": "reduce_21",
            "case": "reduce_21",
            "ID": "reduce_21",
            "return": "reduce_21",
            "switch": "reduce_21",
            ";": "reduce_21"
        },
        "141": {
            ";": "shift_42",
            "(": "shift_43",
            "{": "shift_32",
            "break": "shift_45",
            "if": "shift_46",
            "while": "shift_47",
            "return": "shift_48",
            "switch": "shift_49",
            "compound_stmt": "goto_50",
            "statement": "goto_51",
            "expression_stmt": "goto_52",
            "selection_stmt": "goto_53",
            "iteration_stmt": "goto_54",
            "return_stmt": "goto_55",
            "switch_stmt": "goto_56",
            "expression": "goto_57",
            "var": "goto_58",
            "simple_expression": "goto_59",
            "additive_expression": "goto_60",
            "term": "goto_61",
            "factor": "goto_62",
            "call": "goto_63",
            "p_id": "goto_64",
            "p_num_temp": "goto_65",
            "NUM": "reduce_71",
            "ID": "reduce_70",
            "default": "reduce_39",
            "case": "reduce_39"
        }
    }
}