class CmdInfo:
    def __init__(self, cmd_title, cmd_enter_options, cmd_description):
        self.title = cmd_title
        self.enter_options = cmd_enter_options
        self.description = cmd_description

    def __str__(self):
        options_str = str(self.enter_options).removeprefix('[').removesuffix(']').replace(', ', ' or ')
        return \
f"""  {self.title}:  {self.description}
---------------------------------------------------------------------------
  enter: {options_str}

"""