%token NUM
%token ID
%start program
%%
program: declaration_list
;
declaration_list: declaration_list declaration
| declaration
;
declaration: var_declaration 
| fun_declaration 
;
var_declaration: type_specifier p_id_index ID ';'
| type_specifier p_id_index ID '[' p_num NUM ']' ';'
;
type_specifier: p_label "int"
| p_label "void"
;
fun_declaration: type_specifier p_id_index ID func_declare '(' params ')' compound_stmt
;
params: param_list
| p_label "void"
;
param_list: param_list ',' param
| param
;
param: type_specifier p_id_index ID
| type_specifier p_id_index ID '[' ']'
;
compound_stmt: '{' local_declarations statement_list '}'
;
local_declarations: local_declarations var_declaration
| /* epsilon */
;
statement_list: statement_list statement
| /* epsilon */
;
statement: expression_stmt
| compound_stmt
| selection_stmt
| iteration_stmt
| return_stmt
| switch_stmt
;
expression_stmt: expression ';'
| "break" ';'
| ';'
;
selection_stmt: "if" '(' expression ')' save statement "endif"
| "if" '(' expression ')' save statement "else" jpf_save statement "endif"
;
iteration_stmt: "while" save save_break_temp '(' expression ')' while_condition statement
;
return_stmt: "return" ';'
| "return" expression ';'
;
switch_stmt: "switch" save save_break_temp '(' expression ')' dummy_save '{' case_stmts default_stmt '}'
;
case_stmts: case_stmts case_stmt
| /* epsilon */
;
case_stmt: jpf "case" case_condition NUM ':' save statement_list
;
default_stmt: jpf "default" ':' statement_list
| jpf
;
expression: var '=' expression
| simple_expression
;
var: p_id ID
| p_id ID '[' expression ']'
;
simple_expression: additive_expression relop additive_expression
| additive_expression
;
relop: p_label '<'
| p_label "=="
;
additive_expression: additive_expression addop term
| term
;
addop: p_label '+'
| p_label '-'
;
term: term mulop factor
| factor
;
mulop: p_label '*'
| p_label '/'
;
factor: '(' expression ')'
| var
| call
| p_num_temp NUM
;
call: p_id ID '(' args ')'
;
args: arg_list
| /* epsilon */
;
arg_list: arg_list ',' expression
| expression
;
p_id_index: /* epsilon */
;
p_num: /* epsilon */
;
p_label: /* epsilon */
;
p_id: /* epsilon */
;
p_num_temp: /* epsilon */
;
func_declare: /* epsilon */
;
save: /* epsilon */
;
jpf_save: /* epsilon */
;
save_break_temp: /* epsilon */
;
while_condition: /* epsilon */
;
case_condition: /* epsilon */
;
dummy_save: /* epsilon */
;
jpf: /* epsilon */
;
%%
