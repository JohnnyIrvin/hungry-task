# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from typing import Dict
from uuid import uuid4


class Entity:
    """
    Domain Model based on domain driven design.
    """
    id: uuid4 = uuid4()

    def __eq__(self, o: object) -> bool:
        """
        Dunder method for comparing objects.

        Args:
            o (object): Object to compare.

        Returns:
            bool: True if entity ids are equal, False otherwise.
        """        
        if not isinstance(o, Entity):
            return False
        
        return str(self.id) == str(o.id)

    def __ne__(self, o: object) -> bool:
        """
        Dunder method for comparing objects.

        Args:
            o (object): Object to compare.

        Returns:
            bool: True if entity ids are not equal, False otherwise.
        """
        return not self.__eq__(o)

    def __hash__(self) -> int:
        """
        Hash dunder method.

        Returns:
            int: Entity id.
        """
        return hash(self.id)

    def to_dict(self) -> Dict:
        """
        Convert entity to dictionary.

        Returns:
            Dict: Entity attributes.
        """
        return {"id": self.id, **vars(self)}
