// Initialize the terminal
const term = new Terminal({
    cursorBlink: true,
    theme: {
        background: '#1e1e1e',
        foreground: '#f0f0f0'
    }
});

const fitAddon = new FitAddon.FitAddon();
term.loadAddon(fitAddon);

// Open terminal and make it fit the container
term.open(document.getElementById('terminal'));
fitAddon.fit();

// Store input line
let currentLine = '';
let history = [];
let historyIndex = 0;

// Initialize Pyodide
async function initPyodide() {
    let pyodide = await loadPyodide();
    await pyodide.loadPackagesFromImports(`
    import sys
    import io
  `);

    // Redirect stdout to capture print statements
    pyodide.runPython(`
    class WebConsole:
        def __init__(self, terminal):
            self.terminal = terminal
            self.buffer = ""
        
        def write(self, text):
            self.buffer += text
            if '\\n' in self.buffer:
                lines = self.buffer.split('\\n')
                self.buffer = lines.pop()
                for line in lines:
                    self.terminal.write(line + '\\r\\n')
            return len(text)
        
        def flush(self):
            if self.buffer:
                self.terminal.write(self.buffer)
                self.buffer = ""
    
    sys.stdout = WebConsole(js.term)
    sys.stderr = WebConsole(js.term)
  `);

    // Load your LMS.py code
    const response = await fetch('LMS.py');
    const lmsCode = await response.text();

    // Create input function that will prompt the user
    pyodide.globals.set("get_input", function(prompt) {
        return new Promise((resolve) => {
            term.write(prompt);
            let input = '';

            const inputHandler = term.onData(e => {
                const printable = !e.altKey && !e.ctrlKey && !e.metaKey;

                if (e.charCodeAt(0) === 13) { // Enter key
                    term.write('\r\n');
                    term.off('data', inputHandler);
                    resolve(input);
                } else if (e.charCodeAt(0) === 8) { // Backspace
                    if (input.length > 0) {
                        input = input.substring(0, input.length - 1);
                        term.write('\b \b');
                    }
                } else if (printable) {
                    input += e;
                    term.write(e);
                }
            });
        });
    });

    // Replace Python's input function
    pyodide.runPython(`
    def input_with_prompt(prompt=''):
        return get_input(prompt)
    
    __builtins__.input = input_with_prompt
  `);

    // Run your LMS.py code
    term.write('Loading Logistics Management System...\r\n');
    try {
        await pyodide.runPythonAsync(lmsCode);
    } catch (error) {
        term.write(`\r\nError: ${error}\r\n`);
    }
}

// Start the terminal and Pyodide
term.write('Initializing Python environment...\r\n');
initPyodide().catch(e => {
    term.write(`\r\nFailed to initialize Python: ${e}\r\n`);
});