import ast

SPECIAL_FORMS = ['if', 'define']

BINOPS = {
  '+': ast.Add,
  '-': ast.Sub,
  '/': ast.Div,
  '*': ast.Mult,
  '%': ast.Mod,
}

COMPARES = {
  '=': ast.Eq,
  '!=': ast.NotEq,
  '<': ast.Lt,
  '<=': ast.LtE,
  '>': ast.Gt,
  '>=': ast.GtE,
}


def make_module(function_asts, main_ast):
  module_body = function_asts
  module_body.append(ast.Expr(value=main_ast))
  module_ast = ast.Module(body=module_body)
  ast.fix_missing_locations(module_ast)
  return module_ast
