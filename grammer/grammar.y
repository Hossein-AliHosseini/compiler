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
var_declaration: type_specifier p_id_symbol ID ';'
| type_specifier p_id_symbol ID '[' p_num NUM ']' ';'
;
type_specifier: p_type "int"
| p_type "void"
;
fun_declaration: type_specifier p_id_symbol ID '(' params ')' fun_declare compound_stmt
;
params: param_list
| p_type "void"
;
param_list: param_list ',' param
| param
;
param: type_specifier ID
| type_specifier ID '[' ']'
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
relop: p_operand '<'
| p_operand "=="
;
additive_expression: additive_expression addop term
| term
;
addop: p_operand '+'
| p_operand '-'
;
term: term mulop factor
| factor
;
mulop: p_operand '*'
| p_operand '/'
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
p_operand: /* epsilon */
;
p_num: /* epsilon */
;
p_type: /* epsilon */
;
p_id: /* epsilon */
;
p_id_symbol: /* epsilon */
;
fun_declare: /* epsilon */
;
p_num_temp: /* epsilon */
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
