class CmdInfo:
    def __init__(self, cmd_title, cmd_enter_options, cmd_description, cmd_example):
        self.title = cmd_title
        self.enter_options = cmd_enter_options
        self.description = cmd_description
        self.examples = cmd_example

    def __get_str_examples(self):
      str_examples = ''
      for example in self.examples:
        str_examples += f"\n    : {example}"
      return str_examples

    def __str__(self):
        options_str = str(self.enter_options).removeprefix('[').removesuffix(']').replace(', ', ' or ')
        if len(self.examples) > 1:
          examples_title = "example entries"
        else:
          examples_title = "example entry"
        return \
f"""  -----------------------------------------------------------------------
    {self.title} => {self.description}
   _____________________________________________________________________
    usage
    : {options_str}
   _____________________________________________________________________
    {examples_title}{self.__get_str_examples()}
  -----------------------------------------------------------------------

"""