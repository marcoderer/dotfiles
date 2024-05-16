-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
--
-- TODO: keymappings for tab in insert mode, to use for excepting autocomp suggestions a.s.o

function Map(mode, lhs, rhs, opts)
  local options = { noremap = true, silent = true }
  if opts then
    options = vim.tbl_extend("force", options, opts)
  end
  vim.keymap.set(mode, lhs, rhs, options)
end
--
-- Map("n", "<C-h>", "<C-w>h")
-- Map("n", "<C-j>", "<C-w>j")
-- Map("n", "<C-k>", "<C-w>k")
-- Map("n", "<C-l>", "<C-w>l")
Map("n", "<space>fB", ":Telescope file_browser<CR>", { desc = "File browser" })
Map("n", "<leader>Z", require("telescope").extensions.zoxide.list, { desc = "Zoxide" })
Map("n", "<space>fC", ":Telescope file_browser path=%:p:h select_buffer=true<CR>", { desc = "File browser curr buff" })
Map("n", "<C-p>", ":lua require'telescope'.extensions.project.project{}<CR>")
Map({ "n", "v" }, "HH", "0", { desc = "Easier to start of line" })
Map({ "n", "v" }, "H", "^", { desc = "Easier to first character of line" })
Map({ "n", "v" }, "L", "$", { desc = "Easier to end of line" })
Map({ "n", "v" }, "JJ", "6j", { desc = "Move down faster" })
Map({ "n", "v" }, "KK", "6k", { desc = "Move up faster" })
Map({ "n", "v", "i" }, "<A-l>", "<cmd>tabnext<cr>")
Map({ "n", "v", "i" }, "<A-h>", "<cmd>tabprevious<cr>")
Map("n", ",", "@")
Map("n", ",,", "@@")
Map("i", "jj", "<c-o>:call search('}\\|)\\|]\\|>\\|\"', 'cW')<cr><Right>", { desc = "Jump out of closing bracket" })
Map("i", "jk", "<C-o>a", { desc = "Jump one char to the right" })
Map("i", "kj", "<ESC>:w<CR>")
Map("i", "kk", "<ESC>")
Map("n", "kj", ":w<CR>")
