-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
vim.api.nvim_set_keymap(
  "n",
  "<C-p>",
  ":lua require'telescope'.extensions.project.project{}<CR>",
  { noremap = true, silent = true }
)
vim.keymap.set("n", "<leader>Z", require("telescope").extensions.zoxide.list, { desc = "Zoxide" })
vim.keymap.set("n", "<space>fB", ":Telescope file_browser<CR>", { desc = "File browser" })
-- open file_browser with the path of the current buffer
vim.keymap.set(
  "n",
  "<space>fC",
  ":Telescope file_browser path=%:p:h select_buffer=true<CR>",
  { desc = "File browser curr buff" }
)
vim.keymap.set("n", "<leader>h", require("nvim-highlight-colors").toggle, { desc = "toggle highlight colors" })
