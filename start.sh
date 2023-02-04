#!/bin/bash

ADDITIONAL_ARGS=""

if [ "$ENVIRONMENT" == "dev" ]; then
    ADDITIONAL_ARGS="$ADDITIONAL_ARGS --reload"
fi

python3 -m uvicorn app.main:app --host 0.0.0.0 --port 80 $ADDITIONAL_ARGS