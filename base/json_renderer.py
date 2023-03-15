from rest_framework import status
from rest_framework.renderers import JSONRenderer

class JSONRendererUtills:
    """ Utills to be used in json renderers
    """
    @staticmethod
    def get_status(code):
        """Get the human readable SNAKE_CASE version of a status code."""
        for name, val in status.__dict__.items():
            if not callable(val) and code is val:
                return name.replace("HTTP_%s_" % code, "")
        return "UNKNOWN"
    
    @classmethod
    def get_error_message(cls, error_dict):
        """Method to get custom error message"""
        response = error_dict[next(iter(error_dict))]
        error_name = next(iter(error_dict))
        if isinstance(response, dict):
            response = cls.get_error_message(response)
        elif isinstance(response, list):
            response_message = response[0]
            if isinstance(response_message, dict):
                response = cls.get_error_message(response_message)
            else:
                response = response[0]

        return response.replace("This", error_name)


class ApiJSONRenderer(JSONRenderer):
    """JSON renderer for a common API response format"""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Modify API response format.
        Example success:
        {
            "code": 200,
            "status": "OK",
            "message": "updated succesfully",
            "data": {
                "name": "name"
            }
        }

        Example error:
        {
            "code": 404,
            "status": "NOT_FOUND",
            "errors":
                {
                    "error_message": "Selected date cannot be a past date",
                    "error_code": "BAD_REQUEST"
                }
        """
        response = renderer_context["response"]

        # Modify the response into a cohesive response format
        modified_data = {
            "success": status.is_success(response.status_code),
        }

        if status.is_client_error(response.status_code) or status.is_server_error(
            response.status_code
        ):
            error_message = ""
            err_title = ""
            err_dev_message = ""
            if isinstance(data, list) and data:
                if isinstance(data[0], dict):
                    error_message = (JSONRendererUtills.get_error_message(data),)
                elif isinstance(data[0], str):
                    error_message = data[0]
            if isinstance(data, dict):

                if data.get("err_title"):
                    err_title = data.get("err_title")

                if data.get("err_dev_message"):
                    err_dev_message = data.get("err_dev_message")

                if data.get("error_message"):
                    error_message = data.get("error_message")
                else:
                    error_message = JSONRendererUtills.get_error_message(data)

            error = {
                "err_title": err_title,
                "error_message": error_message,
                "err_dev_message": err_dev_message,
                "error_code": JSONRendererUtills.get_status(response.status_code)
            }
            modified_data["errors"] = error

        else:
            modified_data["total_count"] = data.get("total_count")
            modified_data["next"] = data.get("next")
            modified_data["previous"] = data.get("previous")
            modified_data["next_page"] = data.get("next_page")
            modified_data["current_page"] = data.get("current_page")
            modified_data["previous_page"] = data.get("previous_page")
            modified_data["previous_page"] = data.get("previous_page")
            modified_data["page_size"] = data.get("page_size")

            if isinstance(data, dict):
                if data.get("data") is not None:
                    modified_data["data"] = data.get("data")
                else:
                    modified_data["data"] = data
            else:
                modified_data["data"] = data

        return super().render(modified_data, accepted_media_type, renderer_context)