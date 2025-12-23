# LLM Ops Platform

A web-based platform to operate, observe, and evaluate LLM-powered knowledge systems.

## What this is
This project is an internal AI operations platform that allows engineers to:
- ingest knowledge sources
- run configurable LLM + RAG pipelines
- inspect retrieved context and prompts
- observe latency, cost, and failures
- compare different pipeline configurations

## Why this exists
LLM systems fail silently in production.
This platform makes failures visible and debuggable.

## Tech Stack
- Frontend: Next.js (TypeScript)
- Backend: FastAPI (Python)
- Vector DB: Qdrant
- DB: PostgreSQL
- LLM: OpenAI API
- Deployment: Docker

## Status
Day 1: Repository and skeleton setup
