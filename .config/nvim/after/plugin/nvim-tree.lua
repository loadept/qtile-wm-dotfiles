require("nvim-tree").setup({
  view = {
    adaptive_size = true,
    side = 'right'
  },
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
      git_placement = "after",
      glyphs = {
        git = {
          ignored = "󰛑"
        },
      },
    },
    indent_markers = {
      enable = false,
    }
  }
})
