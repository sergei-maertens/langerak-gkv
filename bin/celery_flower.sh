#!/bin/bash
exec celery --app rkl --workdir src flower
