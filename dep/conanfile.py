from conans import ConanFile, CMake, tools

class DepConan(ConanFile):
    name = "dep"
    version= "0.0.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports = "CMakeLists.txt"
    exports_sources = "code/src/*"
    requires = [("spdlog/1.9.0")]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
    
    def layout(self):
        pass
     
    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="code/src/")
        self.copy("*.hpp", dst="include", src="code/src/")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["dep"]
