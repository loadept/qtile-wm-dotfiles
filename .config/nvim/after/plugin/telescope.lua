local builtin = require("telescope.builtin")

require("telescope").setup {
  pickers = {
    find_files = {
      hidden = true,
      file_ignore_patterns = {
        "%.git/",
        "node_modules/",
        "venv/",
      }
    }
  },
}

vim.keymap.set('n', '<leader>fa', builtin.find_files, {})
vim.keymap.set('n', '<C-p>', builtin.git_files, {})
vim.keymap.set('n', '<leader>fs', function()
  builtin.grep_string({ search = vim.fn.input("Search > ") })
end)
