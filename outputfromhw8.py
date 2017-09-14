Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help(os)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    help(os)
NameError: name 'os' is not defined
>>> ================================ RESTART ================================
>>> 
>>> help(os)
Help on module os:

NAME
    os - OS routines for Mac, NT, or Posix depending on what system we're on.

DESCRIPTION
    This exports:
      - all functions from posix, nt or ce, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix', 'nt' or 'ce'.
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)
    
    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

CLASSES
    builtins.Exception(builtins.BaseException)
        builtins.OSError
    builtins.tuple(builtins.object)
        nt.times_result
        nt.uname_result
        stat_result
        statvfs_result
        terminal_size
    
    error = class OSError(Exception)
     |  Base class for I/O related errors.
     |  
     |  Method resolution order:
     |      OSError
     |      Exception
     |      BaseException
     |      object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  characters_written
     |  
     |  errno
     |      POSIX exception code
     |  
     |  filename
     |      exception filename
     |  
     |  filename2
     |      second exception filename
     |  
     |  strerror
     |      exception strerror
     |  
     |  winerror
     |      Win32 exception code
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
    
    class stat_result(builtins.tuple)
     |  stat_result: Result from stat, fstat, or lstat.
     |  
     |  This object may be accessed either as a tuple of
     |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
     |  or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
     |  
     |  Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
     |  or st_flags, they are available as attributes only.
     |  
     |  See os.stat for more information.
     |  
     |  Method resolution order:
     |      stat_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  st_atime
     |      time of last access
     |  
     |  st_atime_ns
     |      time of last access in nanoseconds
     |  
     |  st_ctime
     |      time of last change
     |  
     |  st_ctime_ns
     |      time of last change in nanoseconds
     |  
     |  st_dev
     |      device
     |  
     |  st_gid
     |      group ID of owner
     |  
     |  st_ino
     |      inode
     |  
     |  st_mode
     |      protection bits
     |  
     |  st_mtime
     |      time of last modification
     |  
     |  st_mtime_ns
     |      time of last modification in nanoseconds
     |  
     |  st_nlink
     |      number of hard links
     |  
     |  st_size
     |      total size, in bytes
     |  
     |  st_uid
     |      user ID of owner
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 16
     |  
     |  n_sequence_fields = 10
     |  
     |  n_unnamed_fields = 3
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      T.__sizeof__() -- size of T in memory, in bytes
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
    
    class statvfs_result(builtins.tuple)
     |  statvfs_result: Result from statvfs or fstatvfs.
     |  
     |  This object may be accessed either as a tuple of
     |    (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
     |  or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
     |  
     |  See os.statvfs for more information.
     |  
     |  Method resolution order:
     |      statvfs_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  f_bavail
     |  
     |  f_bfree
     |  
     |  f_blocks
     |  
     |  f_bsize
     |  
     |  f_favail
     |  
     |  f_ffree
     |  
     |  f_files
     |  
     |  f_flag
     |  
     |  f_frsize
     |  
     |  f_namemax
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 10
     |  
     |  n_sequence_fields = 10
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      T.__sizeof__() -- size of T in memory, in bytes
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
    
    class terminal_size(builtins.tuple)
     |  A tuple of (columns, lines) for holding terminal window size
     |  
     |  Method resolution order:
     |      terminal_size
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  columns
     |      width of the terminal window in characters
     |  
     |  lines
     |      height of the terminal window in characters
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 2
     |  
     |  n_sequence_fields = 2
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      T.__sizeof__() -- size of T in memory, in bytes
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
    
    class times_result(builtins.tuple)
     |  times_result: Result from os.times().
     |  
     |  This object may be accessed either as a tuple of
     |    (user, system, children_user, children_system, elapsed),
     |  or via the attributes user, system, children_user, children_system,
     |  and elapsed.
     |  
     |  See os.times for more information.
     |  
     |  Method resolution order:
     |      times_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  children_system
     |      system time of children
     |  
     |  children_user
     |      user time of children
     |  
     |  elapsed
     |      elapsed time since an arbitrary point in the past
     |  
     |  system
     |      system time
     |  
     |  user
     |      user time
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 5
     |  
     |  n_sequence_fields = 5
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      T.__sizeof__() -- size of T in memory, in bytes
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
    
    class uname_result(builtins.tuple)
     |  uname_result: Result from os.uname().
     |  
     |  This object may be accessed either as a tuple of
     |    (sysname, nodename, release, version, machine),
     |  or via the attributes sysname, nodename, release, version, and machine.
     |  
     |  See os.uname for more information.
     |  
     |  Method resolution order:
     |      uname_result
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  machine
     |      hardware identifier
     |  
     |  nodename
     |      name of machine on network (implementation-defined)
     |  
     |  release
     |      operating system release
     |  
     |  sysname
     |      operating system name
     |  
     |  version
     |      operating system version
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 5
     |  
     |  n_sequence_fields = 5
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  __sizeof__(...)
     |      T.__sizeof__() -- size of T in memory, in bytes
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.

FUNCTIONS
    _exit(...)
        _exit(status)
        
        Exit to the system with specified status, without normal exit processing.
    
    abort(...)
        abort() -> does not return!
        
        Abort the interpreter immediately.  This 'dumps core' or otherwise fails
        in the hardest way possible on the hosting operating system.
    
    access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
        Use the real uid/gid to test for access to a path.
        
          path
            Path to be tested; can be string, bytes, or open-file-descriptor int.
          mode
            Operating-system mode bitfield.  Can be F_OK to test existence,
            or the inclusive-OR of R_OK, W_OK, and X_OK.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          effective_ids
            If True, access will use the effective uid/gid instead of
            the real uid/gid.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            access will examine the symbolic link itself instead of the file
            the link points to.
        
        dir_fd, effective_ids, and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.
        
        Note that most operations will use the effective uid/gid, therefore this
          routine can be used in a suid/sgid environment to test if the invoking user
          has the specified access to the path.
    
    chdir(...)
        chdir(path)
        
        Change the current working directory to the specified path.
        
        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
    
    chmod(...)
        chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
        
        Change the access permissions of a file.
        
        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, chmod will modify the symbolic link itself instead of the file the
          link points to.
        It is an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        dir_fd and follow_symlinks may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    close(...)
        close(fd)
        
        Close a file descriptor (for low level IO).
    
    closerange(...)
        closerange(fd_low, fd_high)
        
        Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    
    cpu_count(...)
        cpu_count() -> integer
        
        Return the number of CPUs in the system, or None if this value cannot be
        established.
    
    device_encoding(...)
        device_encoding(fd) -> str
        
        Return a string describing the encoding of the device
        if the output is a terminal; else return None.
    
    dup(...)
        dup(fd) -> fd2
        
        Return a duplicate of a file descriptor.
    
    dup2(...)
        dup2(old_fd, new_fd)
        
        Duplicate file descriptor.
    
    execl(file, *args)
        execl(file, *args)
        
        Execute the executable file with argument list args, replacing the
        current process.
    
    execle(file, *args)
        execle(file, *args, env)
        
        Execute the executable file with argument list args and
        environment env, replacing the current process.
    
    execlp(file, *args)
        execlp(file, *args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
    
    execlpe(file, *args)
        execlpe(file, *args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env, replacing the current
        process.
    
    execv(...)
        execv(path, args)
        
        Execute an executable path with arguments, replacing current process.
        
            path: path of executable file
            args: tuple or list of strings
    
    execve(...)
        execve(path, args, env)
        
        Execute a path with arguments and environment, replacing current process.
        
            path: path of executable file
            args: tuple or list of arguments
            env: dictionary of strings mapping to strings
        
        On some platforms, you may specify an open file descriptor for path;
          execve will execute the program the file descriptor is open to.
          If this functionality is unavailable, using it raises NotImplementedError.
    
    execvp(file, args)
        execvp(file, args)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args, replacing the current process.
        args may be a list or tuple of strings.
    
    execvpe(file, args, env)
        execvpe(file, args, env)
        
        Execute the executable file (which is searched for along $PATH)
        with argument list args and environment env , replacing the
        current process.
        args may be a list or tuple of strings.
    
    fdopen(fd, *args, **kwargs)
        # Supply os.fdopen()
    
    fsdecode(filename)
        Decode filename from the filesystem encoding with 'surrogateescape' error
        handler, return str unchanged. On Windows, use 'strict' error handler if
        the file system encoding is 'mbcs' (which is the default encoding).
    
    fsencode(filename)
        Encode filename to the filesystem encoding with 'surrogateescape' error
        handler, return bytes unchanged. On Windows, use 'strict' error handler if
        the file system encoding is 'mbcs' (which is the default encoding).
    
    fstat(...)
        fstat(fd) -> stat result
        
        Like stat(), but for an open file descriptor.
        Equivalent to stat(fd=fd).
    
    fsync(...)
        fsync(fildes)
        
        force write of file with filedescriptor to disk.
    
    get_exec_path(env=None)
        Returns the sequence of directories that will be searched for the
        named executable (similar to a shell) when launching a process.
        
        *env* must be an environment variable dict or None.  If *env* is None,
        os.environ will be used.
    
    get_handle_inheritable(...)
        get_handle_inheritable(fd) -> bool
        
        Get the close-on-exe flag of the specified file descriptor.
    
    get_inheritable(...)
        get_inheritable(fd) -> bool
        
        Get the close-on-exe flag of the specified file descriptor.
    
    get_terminal_size(...)
        Return the size of the terminal window as (columns, lines).
        
        The optional argument fd (default standard output) specifies
        which file descriptor should be queried.
        
        If the file descriptor is not connected to a terminal, an OSError
        is thrown.
        
        This function will only be defined if an implementation is
        available for this system.
        
        shutil.get_terminal_size is the high-level function which should 
        normally be used, os.get_terminal_size is the low-level implementation.
    
    getcwd(...)
        getcwd() -> path
        
        Return a unicode string representing the current working directory.
    
    getcwdb(...)
        getcwdb() -> path
        
        Return a bytes string representing the current working directory.
    
    getenv(key, default=None)
        Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are str.
    
    getlogin(...)
        getlogin() -> string
        
        Return the actual login name.
    
    getpid(...)
        getpid() -> pid
        
        Return the current process id
    
    getppid(...)
        getppid() -> ppid
        
        Return the parent's process id.  If the parent process has already exited,
        Windows machines will still return its id; others systems will return the id
        of the 'init' process (1).
    
    isatty(...)
        isatty(fd) -> bool
        
        Return True if the file descriptor 'fd' is an open file descriptor
        connected to the slave end of a terminal.
    
    kill(...)
        kill(pid, sig)
        
        Kill a process with a signal.
    
    link(...)
        link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
        
        Create a hard link to a file.
        
        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        If follow_symlinks is False, and the last element of src is a symbolic
          link, link will create a link to the symbolic link itself instead of the
          file the link points to.
        src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
          platform.  If they are unavailable, using them will raise a
          NotImplementedError.
    
    listdir(...)
        listdir(path='.') -> list_of_filenames
        
        Return a list containing the names of the files in the directory.
        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.
        
        path can be specified as either str or bytes.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        On some platforms, path may also be specified as an open file descriptor;
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.
    
    lseek(...)
        lseek(fd, pos, how) -> newpos
        
        Set the current position of a file descriptor.
        Return the new cursor position in bytes, starting from the beginning.
    
    lstat(...)
        lstat(path, *, dir_fd=None) -> stat result
        
        Like stat(), but do not follow symbolic links.
        Equivalent to stat(path, follow_symlinks=False).
    
    makedirs(name, mode=511, exist_ok=False)
        makedirs(name [, mode=0o777][, exist_ok=False])
        
        Super-mkdir; create a leaf directory and all intermediate ones.  Works like
        mkdir, except that any intermediate path segment (not just the rightmost)
        will be created if it does not exist. If the target directory already
        exists, raise an OSError if exist_ok is False. Otherwise no exception is
        raised.  This is recursive.
    
    mkdir(...)
        mkdir(path, mode=0o777, *, dir_fd=None)
        
        Create a directory.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        
        The mode argument is ignored on Windows.
    
    open(...)
        open(path, flags, mode=0o777, *, dir_fd=None)
        
        Open a file for low level IO.  Returns a file handle (integer).
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    pipe(...)
        pipe() -> (read_end, write_end)
        
        Create a pipe.
    
    popen(cmd, mode='r', buffering=-1)
        # Supply os.popen()
    
    putenv(...)
        putenv(key, value)
        
        Change or add an environment variable.
    
    read(...)
        read(fd, buffersize) -> bytes
        
        Read a file descriptor.
    
    readlink(...)
        readlink(path, *, dir_fd=None) -> path
        
        Return a string representing the path to which the symbolic link points.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    remove(...)
        remove(path, *, dir_fd=None)
        
        Remove a file (same as unlink()).
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    removedirs(name)
        removedirs(name)
        
        Super-rmdir; remove a leaf directory and all empty intermediate
        ones.  Works like rmdir except that, if the leaf directory is
        successfully removed, directories corresponding to rightmost path
        segments will be pruned away until either the whole path is
        consumed or an error occurs.  Errors during this latter phase are
        ignored -- they generally mean that a directory was not empty.
    
    rename(...)
        rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
        
        Rename a file or directory.
        
        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    renames(old, new)
        renames(old, new)
        
        Super-rename; create directories as necessary and delete any left
        empty.  Works like rename, except creation of any intermediate
        directories needed to make the new pathname good is attempted
        first.  After the rename, directories corresponding to rightmost
        path segments of the old name will be pruned way until either the
        whole path is consumed or a nonempty directory is found.
        
        Note: this function can fail with the new directory structure made
        if you lack permissions needed to unlink the leaf directory or
        file.
    
    replace(...)
        replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
        
        Rename a file or directory, overwriting the destination.
        
        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    rmdir(...)
        rmdir(path, *, dir_fd=None)
        
        Remove a directory.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    set_handle_inheritable(...)
        set_handle_inheritable(fd, inheritable)
        
        Set the inheritable flag of the specified handle.
    
    set_inheritable(...)
        set_inheritable(fd, inheritable)
        
        Set the inheritable flag of the specified file descriptor.
    
    spawnl(mode, file, *args)
        spawnl(mode, file, *args) -> integer
        
        Execute file with arguments from args in a subprocess.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnle(mode, file, *args)
        spawnle(mode, file, *args, env) -> integer
        
        Execute file with arguments from args in a subprocess with the
        supplied environment.
        If mode == P_NOWAIT return the pid of the process.
        If mode == P_WAIT return the process's exit code if it exits normally;
        otherwise return -SIG, where SIG is the signal that killed it.
    
    spawnv(...)
        spawnv(mode, path, args)
        
        Execute the program 'path' in a new process.
        
            mode: mode of process creation
            path: path of executable file
            args: tuple or list of strings
    
    spawnve(...)
        spawnve(mode, path, args, env)
        
        Execute the program 'path' in a new process.
        
            mode: mode of process creation
            path: path of executable file
            args: tuple or list of arguments
            env: dictionary of strings mapping to strings
    
    startfile(...)
        startfile(filepath [, operation]) - Start a file with its associated
        application.
        
        When "operation" is not specified or "open", this acts like
        double-clicking the file in Explorer, or giving the file name as an
        argument to the DOS "start" command: the file is opened with whatever
        application (if any) its extension is associated.
        When another "operation" is given, it specifies what should be done with
        the file.  A typical operation is "print".
        
        startfile returns as soon as the associated application is launched.
        There is no option to wait for the application to close, and no way
        to retrieve the application's exit status.
        
        The filepath is relative to the current directory.  If you want to use
        an absolute path, make sure the first character is not a slash ("/");
        the underlying Win32 ShellExecute function doesn't work if it is.
    
    stat(path, *, dir_fd=None, follow_symlinks=True)
        Perform a stat system call on the given path.
        
          path
            Path to be examined; can be string, bytes, or open-file-descriptor int.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be a relative string; path will then be relative to
            that directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            stat will examine the symbolic link itself instead of the file
            the link points to.
        
        dir_fd and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.
        
        It's an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
    
    stat_float_times(...)
        stat_float_times([newval]) -> oldval
        
        Determine whether os.[lf]stat represents time stamps as float objects.
        If newval is True, future calls to stat() return floats, if it is False,
        future calls return ints. 
        If newval is omitted, return the current setting.
    
    strerror(...)
        strerror(code) -> string
        
        Translate an error code to a message string.
    
    symlink(...)
        symlink(src, dst, target_is_directory=False, *, dir_fd=None)
        
        Create a symbolic link pointing to src named dst.
        
        target_is_directory is required on Windows if the target is to be
          interpreted as a directory.  (On Windows, symlink requires
          Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
          target_is_directory is ignored on non-Windows platforms.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    system(...)
        system(command) -> exit_status
        
        Execute the command (a string) in a subshell.
    
    times(...)
        times() -> times_result
        
        Return an object containing floating point numbers indicating process
        times.  The object behaves like a named tuple with these fields:
          (utime, stime, cutime, cstime, elapsed_time)
    
    umask(...)
        umask(new_mask) -> old_mask
        
        Set the current numeric umask and return the previous umask.
    
    unlink(...)
        unlink(path, *, dir_fd=None)
        
        Remove a file (same as remove()).
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
    
    urandom(...)
        urandom(n) -> str
        
        Return n random bytes suitable for cryptographic use.
    
    utime(...)
        utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)
        Set the access and modified time of path.
        
        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        
        If times is not None, it must be a tuple (atime, mtime);
            atime and mtime should be expressed as float seconds since the epoch.
        If ns is not None, it must be a tuple (atime_ns, mtime_ns);
            atime_ns and mtime_ns should be expressed as integer nanoseconds
            since the epoch.
        If both times and ns are None, utime uses the current time.
        Specifying tuples for both times and ns is an error.
        
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, utime will modify the symbolic link itself instead of the file the
          link points to.
        It is an error to use dir_fd or follow_symlinks when specifying path
          as an open file descriptor.
        dir_fd and follow_symlinks may not be available on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
    
    waitpid(...)
        waitpid(pid, options) -> (pid, status << 8)
        
        Wait for completion of a given process.  options is ignored on Windows.
    
    walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple
        
            dirpath, dirnames, filenames
        
        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).
        
        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).
        
        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune
        the search, or to impose a specific order of visiting.  Modifying
        dirnames when topdown is false is ineffective, since the directories in
        dirnames have already been generated by the time dirnames itself is
        generated.
        
        By default errors from the os.listdir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.
        
        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.
        
        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.
        
        Example:
        
        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum([getsize(join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
    
    write(...)
        write(fd, data) -> byteswritten
        
        Write bytes to a file descriptor.

DATA
    F_OK = 0
    O_APPEND = 8
    O_BINARY = 32768
    O_CREAT = 256
    O_EXCL = 1024
    O_NOINHERIT = 128
    O_RANDOM = 16
    O_RDONLY = 0
    O_RDWR = 2
    O_SEQUENTIAL = 32
    O_SHORT_LIVED = 4096
    O_TEMPORARY = 64
    O_TEXT = 16384
    O_TRUNC = 512
    O_WRONLY = 1
    P_DETACH = 4
    P_NOWAIT = 1
    P_NOWAITO = 3
    P_OVERLAY = 2
    P_WAIT = 0
    R_OK = 4
    SEEK_CUR = 1
    SEEK_END = 2
    SEEK_SET = 0
    TMP_MAX = 32767
    W_OK = 2
    X_OK = 1
    __all__ = ['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', ...
    altsep = '/'
    curdir = '.'
    defpath = r'.;C:\bin'
    devnull = 'nul'
    environ = environ({'PROCESSOR_LEVEL': '6', 'COMMONPROGRAMF... 'PROGRAM...
    extsep = '.'
    linesep = '\r\n'
    name = 'nt'
    pardir = '..'
    pathsep = ';'
    sep = r'\'
    supports_bytes_environ = False

FILE
    c:\python34\lib\os.py


>>> os.file.path.getsize("c:\\testfolder\count.txt")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.file.path.getsize("c:\\testfolder\count.txt")
AttributeError: 'module' object has no attribute 'file'
>>> os.path.getsize("c:\\testfolder\count.txt")
90
>>> os.path.getsize("c:\\testfolder")
0
>>> ================================ RESTART ================================
>>> 
>>> space_h("c:\\testfolder\count.txt")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    space_h("c:\\testfolder\count.txt")
  File "C:\Python34\hw8.py", line 59, in space_h
    for name in os.listdir(fname):#name of files in path
NotADirectoryError: [WinError 267] The directory name is invalid: 'c:\\testfolder\\count.txt'
>>> space_h("c:\\testfolder")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    space_h("c:\\testfolder")
  File "C:\Python34\hw8.py", line 64, in space_h
    filesz += count(subname)
NameError: name 'count' is not defined
>>> ================================ RESTART ================================
>>> 
>>> space_h("c:\\testfolder")
180
>>> ================================ RESTART ================================
>>> 
>>> space("c:\\testfolder")
c:\testfolder takes 0MB
>>> space("c:\\python34)
      
SyntaxError: EOL while scanning string literal
>>> space("c:\\python34")
c:\python34 takes 72MB
>>> ================================ RESTART ================================
>>> 
>>> depth("c:\\testfolder")
3
>>> depth("c:\\python34)
      
SyntaxError: EOL while scanning string literal
>>> depth("c:\\python34")
11
>>> ================================ RESTART ================================
>>> 
>>> path("c:\\python34")
(11, 'c:\\python34\\Lib\\site-packages\\pip\\_vendor\\requests\\packages\\urllib3\\packages\\ssl_match_hostname\\__pycache__')
>>> 
