require('gitsigns').setup({
  current_line_blame = true,
  current_line_blame_opts = {
    delay = 300
  },
  current_line_blame_formatter = '    <author>, <author_time:%R>   <summary>',
})

vim.keymap.set("n", "<leader>gp", ":Gitsigns prev_hunk<CR>")
vim.keymap.set("n", "<leader>gn", ":Gitsigns next_hunk<CR>")
vim.keymap.set("n", "<leader>gh", ":Gitsigns preview_hunk<CR>")
vim.keymap.set("n", "<leader>gd", ":Gitsigns diffthis<CR>")
vim.keymap.set("n", "<leader>gr", ":Gitsigns reset_hunk<CR>")
vim.keymap.set("n", "<leader>gb", ":Gitsigns blame_line<CR>")
