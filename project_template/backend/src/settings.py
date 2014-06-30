# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton.gae.middleware.json_middleware import JsonResponseMiddleware
from tekton.gae.middleware.redirect import RedirectMiddleware
from tmpl_middleware import TemplateMiddleware, TemplateWriteMiddleware
from tekton.gae.middleware.email_errors import EmailMiddleware
from tekton.gae.middleware.parameter import RequestParamsMiddleware
from tekton.gae.middleware.router_middleware import RouterMiddleware, ExecutionMiddleware
from tekton.gae.middleware.webapp2_dependencies import Webapp2Dependencies

SENDER_EMAIL = 'renzon@gmail.com'
WEB_BASE_PACKAGE = "web"
TEMPLATE_404_ERROR = 'error.html'
TEMPLATE_400_ERROR = 'error.html'
MIDDLEWARES = [TemplateMiddleware,
               EmailMiddleware,
               Webapp2Dependencies,
               RequestParamsMiddleware,
               RouterMiddleware,
               ExecutionMiddleware,
               TemplateWriteMiddleware,
               JsonResponseMiddleware,
               RedirectMiddleware]

