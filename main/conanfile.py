from conans import ConanFile, CMake, tools

class MainConan(ConanFile):
    name = "main"
    version = "0.0.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "CMakeLists.txt"
    exports_sources = "code/src/*"
    requires = [("dep/0.0.0@user/channel")]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder=".")
        cmake.build()
