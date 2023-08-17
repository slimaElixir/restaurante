class CheckValuesUtils:
    @staticmethod
    def non_empty(value):
        if not value:
            raise ValueError('{} Nao deve estar vazio!'.format(value))
        
    @staticmethod
    def non_empties(values:list):
        for value in values:
            CheckValuesUtils.non_empty(value)