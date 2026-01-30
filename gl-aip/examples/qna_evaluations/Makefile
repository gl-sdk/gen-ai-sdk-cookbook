.PHONY: install help

# Default target
install:
	@echo "📦 Installing dependencies via poetry..."
	poetry config http-basic.gen-ai oauth2accesstoken "$$(gcloud auth print-access-token)"
	poetry config http-basic.gen-ai-internal oauth2accesstoken "$$(gcloud auth print-access-token)"
	poetry config http-basic.gen-ai-publication oauth2accesstoken "$$(gcloud auth print-access-token)"
	poetry config http-basic.gen-ai-internal-publication oauth2accesstoken "$$(gcloud auth print-access-token)"
	poetry install --all-extras
	@echo "✅ Dependencies installed successfully"

help:
	@echo "Available targets:"
	@echo "  make install              - Install all dependencies via poetry"
	@echo "  make help                 - Show this help message"
