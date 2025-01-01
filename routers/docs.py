from fastapi import APIRouter

from services.docs import CONFIG, get_word_counts

docs_router = APIRouter()


@docs_router.get("/counts")
def word_counts():
    """Get word counts for all documents in the app's config."""
    word_counts = get_word_counts(config=CONFIG)
    total = sum(list(word_counts.values()))
    return {
        "word_counts": word_counts,
        "total": total,
    }
