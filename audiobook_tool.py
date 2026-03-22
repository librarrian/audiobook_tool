from absl import app
from absl import flags
from absl import logging
import audiobook_tool

FLAGS = flags.FLAGS
flags.DEFINE_string(
    "asin",
    None,
    "Amazon Standard Identification Number. Used to look up metadata from Audible",
    required=True,
)
flags.DEFINE_bool(
    "merge",
    False,
    "Whether to merge the files found in the input directory into a single m4b file. Can also be used to convert the input file to an m4b file.",
)
flags.DEFINE_alias("m", "merge")
flags.DEFINE_bool(
    "get_chapters",
    True,
    "Whether to get chapter data from Audnexus API. If false, will use the chapter data from the input file.",
)
flags.DEFINE_enum(
    "logging", "error", ["debug", "info", "warning", "error", "fatal"], "Log level."
)
flags.DEFINE_bool(
    "debug", False, "If true, print out all metadata information, and do nothing else."
)
flags.DEFINE_alias("d", "debug")
flags.DEFINE_bool("force", False, "If true, skip confirmation.")
flags.DEFINE_alias("f", "force")

def main(argv):
    logging.set_verbosity(FLAGS.logging)
    if len(argv) != 3:
        raise app.UsageError("Expected exactly 2 arguments: <input_path> <output_path>")
    audiobook_tool.process_audiobook(input_path=argv[1], output_path=argv[2], asin=FLAGS.asin, get_chapters=FLAGS.get_chapters, merge=FLAGS.merge, debug=FLAGS.debug, force=FLAGS.force)


if __name__ == "__main__":
    app.run(main)
