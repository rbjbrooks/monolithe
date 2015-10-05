# -*- coding: utf-8 -*-
# TODO

from gatdlsession import GATDLSession
from .garoot import GARoot

class SDKInfo (object):

    @classmethod
    def api_version(cls):
        """
            Returns the api version
        """
        return 1.0

    @classmethod
    def api_prefix(cls):
        """
            Returns the api prefix
        """
        return "api"

    @classmethod
    def product_accronym(cls):
        """
            Returns the product accronym
        """
        return "TDL"

    @classmethod
    def product_name(cls):
        """
            Returns the product name
        """
        return "ToDoList"

    @classmethod
    def sdk_class_prefix(cls):
        """
            Returns the api prefix
        """
        return "GA"

    @classmethod
    def sdk_name(cls):
        """
            Returns the sdk name
        """
        return "tdldk"

    @classmethod
    def root_object_class(cls):
        """
            Returns the root object class
        """
        return GARoot

    @classmethod
    def session_class(cls):
        """
            Returns the session object class
        """
        return GATDLSession