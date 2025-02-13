require("nvim-tree").setup({
  git = {
    ignore = false
  },
  filters = {
    dotfiles = false,
    custom = { "^.git$", "^node_modules$", "^venv$" }
  },
  renderer = {
    indent_markers = {
      enable = false,
    }
  }
})
