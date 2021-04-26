import re
from drf_spectacular.openapi import AutoSchema

# after upgrading drf_spectacular from ??? version to 0.15.x the /api/ route prefix is added to operation ids
# this custom AutoSchema class ignored /api/ when inferring operation id

class CustomAutoSchema(AutoSchema):
    IGNORE_PATH_PARTS = ['api']
    def _tokenize_path(self):
        # remove path prefix
        path = re.sub(
            pattern=self.path_prefix,
            repl='',
            string=self.path,
            flags=re.IGNORECASE
        )
        # remove path variables
        path = re.sub(pattern=r'\{[\w\-]+\}', repl='', string=path)
        # cleanup and tokenize remaining parts.
        path = path.rstrip('/').lstrip('/').split('/')
        return [t for t in path if t and t not in self.IGNORE_PATH_PARTS]

    def get_operation_id(self):
        """ override this for custom behaviour """
        tokenized_path = self._tokenize_path()
        # replace dashes as they can be problematic later in code generation
        tokenized_path = [t.replace('-', '_') for t in tokenized_path]


        if self.method.lower() == 'get' and self._is_list_view():
            action = 'list'
        else:
            action = self.method_mapping[self.method.lower()]

        if not tokenized_path:
            tokenized_path.append('root')

        if re.search(r'<drf_format_suffix\w*:\w+>', self.path_regex):
            tokenized_path.append('formatted')

        return '_'.join(tokenized_path + [action])