import os
import sys
import gc
import glob
import shutil
from typing import List, Optional


class ModuleCacheManager:

    @staticmethod
    def clear_modules_by_path(path_patterns: List[str] = None):
        if path_patterns is None:
            return

        path_patterns = [os.path.normpath(path) for path in path_patterns]


        try:
            # Remove modules that have files matching any of the path patterns
            for module_name in list(sys.modules.keys()):
                module = sys.modules[module_name]
                if hasattr(module, '__file__') and module.__file__:
                    try:
                        module_path = os.path.normpath(module.__file__)
                        # Check if module path contains any of the specified patterns
                        if any(pattern in module_path for pattern in path_patterns):
                            del sys.modules[module_name]
                    except (TypeError, AttributeError):
                        pass
        except Exception as e:
            print(f"Error while clearing modules: {e}")

        gc.collect()


    @staticmethod
    def clear_coverage_data():
        try:
            # Clear coverage files
            for pattern in ['.coverage*', 'coverage-*']:
                for file in glob.glob(pattern):
                    try:
                        os.remove(file)
                    except:
                        pass

            # Clear pytest cache
            if os.path.exists('.pytest_cache'):
                shutil.rmtree('.pytest_cache', ignore_errors=True)

            # Clear tmp directory if it exists
            if os.path.exists('tmp'):
                shutil.rmtree('tmp', ignore_errors=True)

            # Reset coverage module
            try:
                import coverage
                cov = coverage.Coverage()
                cov.erase()
            except:
                pass

        except Exception as e:
            print(f"Coverage cleanup warning: {e}")

    @staticmethod
    def cleanup_tmp_folder():
        """Clean up the tmp folder before loading new tests"""
        tmp_dir = 'tmp'
        if os.path.exists(tmp_dir):
            try:
                shutil.rmtree(tmp_dir)
                print(f"Cleaned up existing tmp directory: {tmp_dir}")
            except Exception as e:
                print(f"Warning: Could not clean up {tmp_dir}: {e}")

    @staticmethod
    def clear_all(path_patterns: List[str] = None):
        ModuleCacheManager.cleanup_tmp_folder()
        ModuleCacheManager.clear_modules_by_path(path_patterns)
        ModuleCacheManager.clear_coverage_data()
