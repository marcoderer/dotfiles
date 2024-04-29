return {
  {
    "nvim-telescope/telescope.nvim",
    require("telescope").setup({
      defaults = {
        -- Default configuration for telescope goes here:
        -- config_key = value,
        mappings = {
          i = {
            -- map actions.which_key to <C-h> (default: <C-/>)
            -- actions.which_key shows the mappings for your picker,
            -- e.g. git_{create, delete, ...}_branch for the git_branches picker
            ["<C-h>"] = "which_key",
          },
        },
      },
      pickers = {
        -- Default configuration for builtin pickers goes here:
        -- picker_name = {
        --   picker_config_key = value,
        --   ...
        -- }
        -- Now the picker_config_key will be applied every time you call this
        -- builtin picker
        find_files = {
          -- hidden = true,
          find_command = { "rg", "--files", "--hidden", "--glob", "!**/.git/*" },
        },
      },
      extensions = {
        file_browser = {

          theme = "ivy",
          -- disables netrw and use telescope-file-browser in its place
          hijack_netrw = true,
          mappings = {
            ["i"] = {},
            ["n"] = {
              -- your custom normal mode mappings
            },
          },
        },
        project = {

          base_dirs = {
            "~/dev/js/",
            { "~/dev/python" },
            { "~/dev/rust/", max_depth = 4 },
            { path = "~/dev/nvim" },
            { path = "~/dev/shell/", max_depth = 2 },
          },
          hidden_files = true, -- default: false
          theme = "dropdown",
          order_by = "asc",
          search_by = "title",
          -- default for on_project_selected = find project files
          -- on_project_selected = function(prompt_bufnr)
          -- Do anything you want in here. For example:
          -- project_actions.change_working_directory(prompt_bufnr, false)
          -- require("harpoon.ui").nav_file(1)
          -- end,
        },
      },
    }),
  },

  {
    "nvim-telescope/telescope-symbols.nvim",
  },
  {
    "nvim-lua/popup.nvim",
  },
  {
    "jvgrootveld/telescope-zoxide",
  },
  {
    "nvim-telescope/telescope-file-browser.nvim",
    dependencies = { "nvim-telescope/telescope.nvim", "nvim-lua/plenary.nvim" },
  },
  {
    "nvim-telescope/telescope-project.nvim",
  },
}
