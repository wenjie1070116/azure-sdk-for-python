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
try:
    import collections.abc as collections
except ImportError:
    import collections  # type: ignore

from azure.core.utils import CaseInsensitiveDict

from ._http_response_impl import _HttpResponseBaseImpl, HttpResponseImpl, _HttpResponseBackcompatMixinBase
from ..pipeline.transport._requests_basic import StreamDownloadGenerator


class _RestRequestsTransportResponseBaseMixin(_HttpResponseBackcompatMixinBase):
    """Backcompat mixin for the sync and async requests responses

    Overriding the default mixin behavior here because we need to synchronously
    read the response's content for the async requests responses
    """

    def _body(self):
        # Since requests is not an async library, for backcompat, users should
        # be able to access the body directly without loading it first (like we have to do
        # in aiohttp). So here, we set self._content to self._internal_response.content,
        # which is similar to read, without the async call.
        if self._content is None:
            self._content = self._internal_response.content
        return self._content

class _RestRequestsTransportResponseBase(_HttpResponseBaseImpl, _RestRequestsTransportResponseBaseMixin):
    def __init__(self, **kwargs):
        internal_response = kwargs.pop("internal_response")
        content = None
        if internal_response._content_consumed:
            content = internal_response.content
        headers = CaseInsensitiveDict(internal_response.headers)
        super(_RestRequestsTransportResponseBase, self).__init__(
            internal_response=internal_response,
            status_code=internal_response.status_code,
            headers=headers,
            reason=internal_response.reason,
            content_type=headers.get('content-type'),
            content=content,
            **kwargs
        )

class RestRequestsTransportResponse(HttpResponseImpl, _RestRequestsTransportResponseBase):

    def __init__(self, **kwargs):
        super(RestRequestsTransportResponse, self).__init__(
            stream_download_generator=StreamDownloadGenerator,
            **kwargs
        )
