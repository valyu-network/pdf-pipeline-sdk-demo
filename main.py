from valyu_pipeline.processor import PDFProcessor
import os

# Set 'VALYU-API-KEY' as env var. Contact support@valyu.network for one.
os.environ['VALYU_API_KEY'] = 'YOUR-VALYU-API-KEY'

processor = PDFProcessor()
processor.start_job('<folder path with .pdf files>')