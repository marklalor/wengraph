workspace(name = "wengraph")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.2.0/rules_python-0.2.0.tar.gz",
    sha256 = "778197e26c5fbeb07ac2a2c5ae405b30f6cb7ad1f5510ea6fdac03bded96cc6f",
)

#load("@rules_python//python:pip.bzl", "pip_install")
#
#pip_install(
#   requirements = "//graph/schema/scripts:requirements.txt",
#   quiet = False,
#)

http_file(
  name = "cedict_zip",
  urls = ["https://wengraph.s3.us-west-1.amazonaws.com/external/dictionary/cedict.zip"],
  sha256 = "d61eb266bf82d696f92328841094dc35c987f420a2a82f087d5b296bb202f722",
)