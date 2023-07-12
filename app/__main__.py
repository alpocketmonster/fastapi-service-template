import logging
import sys
import traceback


if __name__ == '__main__':
    try:
        import aioprometheus  # pylint: disable=unused-import
        import pydantic  # pylint: disable=unused-import
        import sentry_sdk  # pylint: disable=unused-import
        import uvicorn

        from sentry_sdk.integrations.asyncio import AsyncioIntegration
        from sentry_sdk.integrations.logging import LoggingIntegration

        from app.config import Config
        from app.logger import logger

        _settings = Config()

        # turn on Sentry
        if _settings.SENTRY_USE:
            logging.info("Starting Sentry")
            sentry_logging = LoggingIntegration(
                level=logging.INFO,
                event_level=logging.ERROR,
            )
            sentry_sdk.init(
                dsn=_settings.SENTRY_DSN,
                integrations=[
                    sentry_logging,
                    AsyncioIntegration(),
                ],
                traces_sample_rate=1.0,
                attach_stacktrace=True,
                request_bodies="always",
            )

        uvicorn.run("main:app", port=_settings.PORT)

    except pydantic.ValidationError as e:
        logging.getLogger().fatal(
            f"The config file is broken - {e}. Service is stopped."
        )
        sys.exit(1)
    except ModuleNotFoundError as e:
        logging.getLogger().fatal(f"Some module is not found - {e}. Service is stopped")
        traceback.print_exc()
        sys.exit(1)
    except Exception as e:  # pylint: disable=broad-except
        logging.getLogger().fatal(f"Unknown error - {e}. Service is stopped")
        traceback.print_exc()
        sys.exit(1)
