import argparse

from keras.callbacks import (
    Callback,
    ModelCheckpoint,
    ProgbarLogger,
    TensorBoard,
)
from keras.models import Model
from keras.optimizers import Adam
from keras.utils import Sequence

from typing import Iterable


def create_config() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--savedir",
        type=str,
        default="save",
        help="Model checkpoint save directory",
    )

    parser.add_argument(
        "--logdir",
        type=str,
        default="save",
        help="TensorBoard logging directory",
    )

    parser.add_argument(
        "-b",
        "--batchsize",
        type=int,
        default=64,
        help="Number of images per training batch",
    )

    parser.add_argument(
        "-e",
        "--epochs",
        type=int,
        default=100,
        help="Number of epochs to train for",
    )

    parser.add_argument(
        "-v",
        "--verbosity",
        type=str,
        default="auto",
        help="Keras training verbosity",
    )

    parser.add_argument(
        "-m",
        "--multiprocessing",
        action="store_true",
        help="Whether data generator should use multiprocessing",
    )

    parser.add_argument(
        "-w",
        "--workers",
        type=int,
        default=1,
        help="Number of workers data generator should use for multiprocessing",
    )

    parser.add_argument(
        "-s",
        "--split",
        type=float,
        default=0.3,
        help="Proportion of data to use as validation set",
    )

    parser.add_argument(
        "--lr",
        type=float,
        default=0.001,
        help="Learning rate to use for training",
    )

    return parser.parse_args()


def create_model(config) -> Model:
    pass


def create_generator(config) -> Sequence:
    pass


def create_callbacks(config) -> Iterable[Callback]:
    update_freq = 10
    return [
        ProgbarLogger(),
        TensorBoard(config.logdir, update_freq=update_freq),
        ModelCheckpoint(config.savedir, save_freq="epoch"),
    ]


def train(
    model: Model,
    generator: Sequence,
    callbacks: Iterable[Callback],
    config: argparse.Namespace,
):

    model.compile(optimizer=Adam(lr=config.lr))
    model.fit(
        x=generator,
        batch_size=config.batch_size,
        epochs=config.epochs,
        validation_split=config.split,
        verbose=config.verbosity,
        callbacks=callbacks,
        use_multiprocessing=config.multiprocessing,
        workers=config.workers,
    )


def main():
    from pprint import pprint

    config = create_config()
    pprint(config)

    callbacks = create_callbacks(config)
    pprint(callbacks)

    """
    model = create_model(config)
    generator = create_generator(config)

    model.compile()
    train(model, generator, callbacks, config)
    """
