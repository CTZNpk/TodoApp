#!/bin/zsh


# Run PostgreSQL container
docker run --rm -d --name test-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 postgres

