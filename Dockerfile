FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml ./
COPY dcom_mcp ./dcom_mcp
RUN pip install --no-cache-dir .
COPY teaching ./teaching
COPY course ./course
COPY Data_Communications ./Data_Communications
ENV COURSE_ROOT=/app MCP_HOST=0.0.0.0 MCP_PORT=8000
USER 65534:65534
EXPOSE 8000
CMD ["dcom-mcp", "--http"]

