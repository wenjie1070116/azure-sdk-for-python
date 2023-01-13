# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from typing import List
from azure.core.pipeline import PipelineRequest, PipelineResponse
from ._base import SansIOHTTPPolicy


class SensitiveHeaderCleanupPolicy(SansIOHTTPPolicy):
    """A simple policy that cleans up sensitive headers

    :keyword List[str] block_headers_list: The headers to clean up.
    :keyword bool not_clean_up_header: Opt out cleaning up sensitive headers
    """
    DEFAULT_SENSITIVE_HEADERS = set(
        [
            "Authorization",
            "x-ms-authorization-auxiliary",
        ]
    )

    def __init__(
        self, *, block_headers_list: List[str] = None, not_clean_up_header: bool = False, **kwargs
    ):  # pylint: super-init-not-called
        self._not_clean_up_header = not_clean_up_header
        self._block_headers_list = \
            SensitiveHeaderCleanupPolicy.DEFAULT_SENSITIVE_HEADERS if block_headers_list is None else block_headers_list

    def on_request(self, request):  # pylint: disable=arguments-differ
        # type: (PipelineRequest) -> None
        """This is executed before sending the request to the next policy.

        :param request: The PipelineRequest object.
        :type request: ~azure.core.pipeline.PipelineRequest
        """
        insecure_domain_change = request.context.options.pop('insecure_domain_change', False)
        if not self._not_clean_up_header and insecure_domain_change:
            for header in self._block_headers_list:
                request.http_request.headers.pop(header, None)

    def on_response(self, request, response):
        # type: (PipelineRequest, PipelineResponse) -> None
        """Executed after the request comes back from the next policy.

        :param request: Request to be modified after returning from the policy.
        :type request: ~azure.core.pipeline.PipelineRequest
        :param response: Pipeline response object
        :type response: ~azure.core.pipeline.PipelineResponse
        """
