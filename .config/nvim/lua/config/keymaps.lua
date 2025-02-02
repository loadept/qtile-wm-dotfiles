vim.g.mapleader = " "

-- Toggle Tree
vim.keymap.set("n", "<leader>e", vim.cmd.NvimTreeToggle)

-- Save with CTRL S
vim.keymap.set("n", "<C-s>", ":w<CR>")
vim.keymap.set("i", "<C-s>", "<Esc>:w<CR>")

vim.keymap.set("n", "<C-q>", ":qa<CR>")
vim.keymap.set("i", "<C-q>", "<Esc>:q<CR>")

-- GO Formater
vim.keymap.set("n", "<A-f>", ":Format<CR>")

vim.keymap.set("n", "<leader>t", ":belowright split +resize-11 | terminal<CR>")
vim.keymap.set("t", "<C-k>", "<C-\\><C-n><C-w>k")
