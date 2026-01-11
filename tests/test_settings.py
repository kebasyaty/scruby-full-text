"""Test a settings module."""

from __future__ import annotations

from scruby_manticore import LANGUAGES


class TestPositive:
    """Positive tests."""

    def test_supported_languages(self) -> None:
        """Testing supported languages."""
        assert LANGUAGES.Arabic == "libstemmer_ar"
