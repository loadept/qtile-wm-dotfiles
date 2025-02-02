require("nvim-tree").setup({
  git = {
    ignore = false
  },
  filters = {
    dotfiles = false
  },
  renderer = {
    indent_markers = {
      enable = false,
    }
  }
})
