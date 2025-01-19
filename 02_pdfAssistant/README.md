# agent will communicate with database to ask queries and get results



Here, in addition to the tools, we will be using external databases.
# we are using PgVector databse and running it in docker


docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16



  # KNOWLEDGE
  it is a database of information that an agent can search to  improve its responses. This information is stored in vector databases and provides agents with business context,  helping them respond in a conteext aware manner.


  # PDFURL Knowledge base
  to load the PDF from URLs.


