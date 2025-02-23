require("nvim-tree").setup({
  git = {
    ignore = false
  },
  filters = {
    dotfiles = false,
    custom = { "^.git$", "^node_modules$", "^venv$" }
  },
  renderer = {
    icons = {
      show = {
        folder_arrow = false,
      },
    },
    indent_markers = {
      enable = false,
    }
  }
})
